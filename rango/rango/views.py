from django.shortcuts import render
from mainapp.models import Category, Page

# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:10]
    context = {'categories' : category_list, 'pages' : page_list}
    return render(request, 'index.html', context)


def about(request):
    context = {'author_name':'Tvoretc'}
    return render(request, 'about.html', context)
