from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( 
        TokenObtainPairView)

from .views import GenresViewSet, CategoriesViewSet, TitlesViewSet

router = DefaultRouter()

router.register('genres', GenresViewSet)
router.register('categories', CategoriesViewSet)
#router.register('categories/(slug)', CategoriesViewSet)
router.register('titles', TitlesViewSet)
router.register('titles/(?P<id>\d+)/reviews', TitlesViewSet)

urlpatterns = [ 
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    #path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('v1/', include(router.urls)), 
] 