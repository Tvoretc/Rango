from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from mainapp.models import Category, Page
from mainapp.forms import CategoryForm, PageForm, UserForm, UserProfileForm

# Create your views here.

def category_detail(request, category_name_slug):
    category = get_object_or_404(Category, slug = category_name_slug)
    category.views = category.views + 1
    category.save()
    pages = Page.objects.filter(category = category)
    context = {'category' : category, 'pages' : pages}
    return render(request, 'mainapp/category_detail.html', context)


@login_required
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


@login_required
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

def register(request):
    reged = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            reged = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'mainapp/register.html',{
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': reged,
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your Rango account is unactive.')
        else:
            print('Invalid login or password: {}  {}'.format(username, password))
            return HttpResponse('Invalid login or password.')
    else:
        return render(request, 'mainapp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
