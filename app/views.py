# Create your views here.
from .models import Category, Video
from .serializers import CategorySerializer, VideoSerializer
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions


class CategoryView(viewsets.ModelViewSet):
    """This view for category"""
    queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


class VideoView(viewsets.ModelViewSet):
    """This view for videos"""
    queryset = Video.objects.filter(published=True)
    serializer_class = VideoSerializer
    authentication_classes = [authentication.TokenAuthentication]

    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        videos = self.queryset.filter(category_id=category_id)
        serializer = self.get_serializer(videos, many=True)
        return Response(serializer.data)
