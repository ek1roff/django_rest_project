from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from blog.views import (BlogAPIList,
                        BlogAPIUpdate,
                        BlogAPIDestroy,
                        BlogHome,
                        ShowPost,
                        about)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('about/', about, name='about'),
    path('api/v1/blog/', BlogAPIList.as_view()),
    path('api/v1/blog/<int:pk>/', BlogAPIUpdate.as_view()),
    path('api/v1/blogdelete/<int:pk>/', BlogAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
