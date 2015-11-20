from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    

