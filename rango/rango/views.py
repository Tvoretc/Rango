from django.shortcuts import render
from mainapp.models import Category, Page

# Create your views here.

def index(request):
    request.session.set_test_cookie()
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:10]
    context = {'categories' : category_list, 'pages' : page_list}
    return render(request, 'index.html', context)


def about(request):
    if request.session.test_cookie_worked():
        print('test cookie worked.')
        request.session.delete_test_cookie()
    context = {'author_name':'Tvoretc'}
    return render(request, 'about.html', context)
