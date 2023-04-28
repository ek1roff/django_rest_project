from django.contrib import admin
from django.urls import path
from blog.views import BlogAPIList, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bloglist/', BlogAPIList.as_view()),
    path('', index, name='index'),
    path('api/v1/bloglist/<int:pk>/', BlogAPIList.as_view()),

]
