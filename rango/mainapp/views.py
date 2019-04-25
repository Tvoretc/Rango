from django.shortcuts import render, redirect
from mainapp.models import Category, Page
from django.shortcuts import get_object_or_404
from mainapp.forms import CategoryForm, PageForm

# Create your views here.

def category_detail(request, category_name_slug):
    category = get_object_or_404(Category, slug = category_name_slug)
    category.views = category.views + 1
    category.save()
    pages = Page.objects.filter(category = category)
    context = {'category' : category, 'pages' : pages}
    return render(request, 'mainapp/category_detail.html', context)


def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    return render(request, 'mainapp/add_category.html', {'form' : form})


def add_page(request, category_name_slug):
    category = get_object_or_404(Category, slug = category_name_slug)

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit = False)
            page.category = category
            page.save()
            return redirect('mainapp:category_detail', category_name_slug = category_name_slug)
        else:
            print(form.errors)
            
    context = {'form':form, 'category':category}
    return render(request, 'mainapp/add_page.html', context)
