from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import User
from .permissions import IsAdminOrMe
from .serializers import (
    ConfirmationCodeSerializer, UserEmailSerializer, UserSerializer
)


@api_view(['POST'])
def get_confirmation_code(request):
    username = request.data.get('username')
    serializer = UserEmailSerializer(data=request.data)
    email = request.data.get('email')
    
    if serializer.is_valid():
        if username:
            username_qs = User.objects.filter(username=username)
            email_qs = User.objects.filter(email=email)
            user = username_qs | email_qs
            if not user:
                User.objects.create_user(username=username, email=email)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        user = get_object_or_404(User, email=email)
        confirmation_code = default_token_generator.make_token(user)
        
        mail_subject = 'Код подтверждения'
        message = f'Ваш {mail_subject.lower()}: {confirmation_code}'
        sender_email = 'Yamdb.ru <admin@yamdb.ru>'
        recipient_email = email
        
        send_mail(
            mail_subject,
            message,
            sender_email,
            [recipient_email],
            fail_silently=False
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_jwt_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.data.get('email')
        confirmation_code = serializer.data.get('confirmation_code')
        user = get_object_or_404(User, email=email)
        
        if default_token_generator.check_token(user, confirmation_code):
            token = AccessToken.for_user(user)
            return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
        
        resp = {'confirmation_code': 'Неверный код подтверждения'}
        return Response(resp, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrMe]
    model = User
    serializer = UserSerializer