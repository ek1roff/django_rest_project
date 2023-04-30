from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import Blog, Category
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# class BlogAPIList(generics.ListCreateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogAPIUpdate(generics.UpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer


def index(request):
    posts = Blog.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'blog/index.html', context)
