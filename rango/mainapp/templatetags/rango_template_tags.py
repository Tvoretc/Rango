from django import template
from mainapp.models import Category

register = template.Library()

@register.inclusion_tag('mainapp/cats.html')
def get_category_list():
    return {'cats':Category.objects.all()}
