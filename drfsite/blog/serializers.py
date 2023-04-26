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

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.content = validated_data.get("content", instance.content)
        instance.photo = validated_data.get("photo", instance.photo)
        #instance.time_create = validated_data.get("time_create", instance.time_create)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()

        return instance


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
