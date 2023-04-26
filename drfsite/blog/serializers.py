from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Blog


# class BlogModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField()
    content = serializers.CharField()
    photo = serializers.ImageField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = BlogModel('Petr I', 'Content: Petr I')
#     model_sr = BlogSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Petr I","content":"Content: Petr I"}')
#     data = JSONParser().parse(stream)
#     serializer = BlogSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
