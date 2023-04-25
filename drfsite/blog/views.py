from django.shortcuts import render
from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


def index(request):
    return render(request, 'blog/index.html', {'title': 'Главная страница'})
