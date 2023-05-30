from django import template
from blog.models import Category, CustomUser

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_users():
    return CustomUser.objects.all()
