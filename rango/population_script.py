import os
from collections import namedtuple
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango.settings')

import django
django.setup()

from mainapp.models import Category, Page

Cat = namedtuple('Cat', ['name', 'views', 'likes', 'pages'])

def populate():
    python_pages = (
        ('Official Python Tutorial', 'https://docs.python.org/2/tutorial/'),
        ('CodingBat', 'https://codingbat.com/python'),
    )

    django_pages = (
        ('Official Django Documeentation', 'https://docs.djangoproject.com/en/2.2/'),
        ('Simple is better than complex', 'https://simpleisbetterthancomplex.com/'),
        ('How to Tango with Django', 'http://www.tangowithdjango.com/'),
    )

    styling_pages = (
        ('Google Fonts', 'https://fonts.google.com/'),
        ('Bootstrap', 'https://getbootstrap.com/docs/4.3/getting-started/introduction/'),
        ('Web School', 'https://www.w3schools.com/'),
    )

    cat_names = ('python','django','styling')
    pages = (python_pages, django_pages, styling_pages)
    categories = [
        Cat(cat_names[i], get_views(i), get_likes(i), pages[i]) for i in range(3)
    ]

    for cat in categories:
        c = add_cat(cat)
        for page in cat.pages:
            print(page)
            add_page(c, page)


def get_likes(k):
    return 2**(7-k)

def get_views(k):
    return 2**(6-k)

def add_page(cat, page):
    p = Page.objects.get_or_create(category = cat, title = page[0], url = page[1])[0]
    p.save()
    print('Saved {} from {}.'.format(cat, p))
    return p

def add_cat(cat):
    c = Category.objects.get_or_create(name = cat.name, views = cat.views, likes = cat.likes)[0]
    c.save()
    return c


if __name__ == '__main__':
    print('Starting population...')
    populate()
    print('Population complete.')
