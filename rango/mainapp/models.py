from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 40, unique = True)
    views = models.PositiveIntegerField(default = 0)
    likes = models.PositiveIntegerField(default = 0)
    slug = models.SlugField(blank = True, unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{}*{}[{}]'.format(self.name,self.views, self.likes)


class Page(models.Model):
    title = models.CharField(max_length = 40)
    views = models.PositiveIntegerField(default = 0)
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return '{}({})'.format(self.title, self.views)


class UserProfile(models.Model):
    """docstring for UserProfile."""
    user = models.OneToOneField(User)
    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __str__(self):
        return self.user.username
