from django.contrib import admin
from django.urls import path
from blog.views import (BlogHome, ShowPost, RegisterUser, BlogCategory,
                        LoginUser, logout_user, addpage, about, ProfilePage, CreateProfilePageView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('about/', about, name='about'),
    #path('addpage/', AddPage.as_view(), name='addpage'),
    path('addpage/', addpage, name='addpage'),
    path('user_profile/<int:pk>/', ProfilePage.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
]
