from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer


class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):
        b = Blog.objects.all()
        return Response({'posts': BlogSerializer(b, many=True).data})

    def post(self, request):
        post_new = Blog.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': BlogSerializer(post_new).data})

def index(request):
    return render(request, 'blog/index.html', {'title': 'Главная страница'})
