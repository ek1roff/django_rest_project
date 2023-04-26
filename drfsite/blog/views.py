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
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exist"})

        serializer = BlogSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

def index(request):
    return render(request, 'blog/index.html', {'title': 'Главная страница'})
