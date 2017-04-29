from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
import datetime


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User)
    post_note = RichTextField(null=True,blank=True)
    post_date = models.DateTimeField(default=datetime.datetime.now(),blank=True,null=True)
    slug = models.SlugField( max_length=100,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "Title: %s    Author: %s    Date: %s " % (self.title , self.author, self.post_date)

    def get_post_title(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super(Post, self).save(*args, **kwargs)
'''
    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.post_id, self.slug())

    def slug(self):
        return slugify(self.title)
'''

