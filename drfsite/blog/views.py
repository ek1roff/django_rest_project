from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Blog, Category
from .serializers import BlogSerializer


class BlogAPIList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


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

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exist"})

        instance.delete()

        return Response({"post": "delete post " + str(pk)})


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
