from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewset import TuristicPointViewSet
from atractions.api.viewsets import AttractionsViewSet
from address.api.viewset import AddressViewSet
from comments.api.viewset import CommentViewSet
from reviews.api.viewset import ReviewViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register(r'turistic-point', TuristicPointViewSet, basename='TuristicPoint')
router.register(r'attractions', AttractionsViewSet)
router.register(r'address', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('sessions', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
