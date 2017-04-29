from django.conf.urls import include, url
from .views import post_view, post_list_view


urlpatterns = [

    url(r'^$', post_list_view, name="post"),
    url(r'^(?P<slug>[\w-]+)/$', post_view, name="post_detail"),
]
