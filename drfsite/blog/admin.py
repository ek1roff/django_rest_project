from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .forms import CustomUserCreationForm, UserUpdateForm
from .models import Blog, Category, CustomUser


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'cat', 'content', 'image', 'is_published',
              'time_create', 'get_html_image', 'user')
    readonly_fields = ('time_create', 'get_html_image')
    save_on_top = True

    def get_html_image(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_image.short_description = 'Изображение'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ['email', 'username',]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

