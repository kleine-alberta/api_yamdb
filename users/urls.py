from django.urls import include, path
from users.views import UserViewSet, get_confirmation_code, get_jwt_token

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router_v1 = DefaultRouter()
router_v1.register('', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('email/', get_confirmation_code, name='token_obtain_pair'),
    path('token/', get_jwt_token, name='token'),
    path(
        'token/refresh/', TokenRefreshView.as_view(),
        name='token_refresh'
    )
]
