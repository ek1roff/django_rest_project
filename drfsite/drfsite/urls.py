from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from blog.views import (BlogAPIList,
                        BlogAPIUpdate,
                        BlogAPIDestroy,
                        index)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('', index, name='index'),
    path('api/v1/blog/', BlogAPIList.as_view()),
    path('api/v1/blog/<int:pk>/', BlogAPIUpdate.as_view()),
    path('api/v1/blogdelete/<int:pk>/', BlogAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
