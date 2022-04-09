from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}


@register.inclusion_tag('blog/sidebar_tpl.html')
def show_categories(sidebar_class='sidebar'):
    categories = Category.objects.all()
    return {"categories": categories, "sidebar_class": sidebar_class}
