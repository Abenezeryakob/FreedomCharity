from django.contrib import admin
from .models import OurChildren
from django.utils.html import format_html


class ImageModelAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style={width:auto; height:200px;}/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag',OurChildren]

class OurChildenAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width ="100" height="100" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    model = OurChildren
    search_fields = ('first_name', 'last_name', 'age')
    list_display = ['first_name', 'last_name', 'age','image_tag']
    list_display_links = ('first_name','age', 'last_name')


class OurChildenProxy(OurChildren):
    class Meta:
        proxy=True

admin.site.register(OurChildren,OurChildenAdmin)


