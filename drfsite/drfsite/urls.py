from django.contrib import admin
from django.urls import path
from blog.views import BlogAPIView, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bloglist/', BlogAPIView.as_view()),
    path('', index, name='index'),
    path('api/v1/bloglist/<int:pk>/', BlogAPIView.as_view()),

]
