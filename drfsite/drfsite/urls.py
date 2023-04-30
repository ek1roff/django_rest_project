from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog.views import (BlogViewSet,
                        index)

router = routers.SimpleRouter()
router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/bloglist/', BlogViewSet.as_view({'get': 'list'})),
    # path('api/v1/bloglist/<int:pk>/', BlogViewSet.as_view({'put': 'update'})),
    # path('api/v1/blogdetail/<int:pk>/', BlogViewSet.as_view({'delete': 'destroy'})),
]
