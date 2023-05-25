from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from blog.views import (BlogAPIList,
                        BlogAPIUpdate,
                        BlogAPIDestroy,
                        BlogHome,
                        ShowPost,
                        about, RegisterUser, LoginUser, logout_user)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('about/', about, name='about'),
    # path('api/v1/blog/', BlogAPIList.as_view()),
    # path('api/v1/blog/<int:pk>/', BlogAPIUpdate.as_view()),
    # path('api/v1/blogdelete/<int:pk>/', BlogAPIDestroy.as_view()),
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
