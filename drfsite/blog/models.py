from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from pytils.translit import slugify
from django.utils.safestring import mark_safe


class CustomUser(AbstractUser):
    slug = AutoSlugField(populate_from='username', unique=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="images/avatars/", default='images/avatars/default.jpg')

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'slug': self.slug})

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name='Изображение',)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Автор')
    slug = AutoSlugField(populate_from='title', unique=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)
