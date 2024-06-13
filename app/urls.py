from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, VideoView
router = DefaultRouter()
router.register('category', CategoryView, basename='category')
router.register('video', VideoView, basename='video')

urlpatterns = [
    path('video-api/', include(router.urls)),
]
