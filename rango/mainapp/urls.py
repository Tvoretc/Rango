from django.conf.urls import url
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    url(r'^add_category/$', views.add_category, name = 'add_category'),
    url(r'^(?P<category_name_slug>[\w\-]+)/$', views.category_detail, name = 'category_detail'),
    url(r'^(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name = 'add_page'),
]
