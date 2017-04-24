from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from django.core.files.base import ContentFile
# Create your models here.

class OurChildren(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    content = RichTextField()

    image = models.ImageField(upload_to = "static/images/our_children")


    def __str__(self):
        return "name: %s - %s" % (self.first_name , self.last_name)

    def get_name(self):
        return (self.first_name)

    def get_thumbnail(self, thumb_size=None):

        base = Image.open(StringIO(self.image.read()))  # get the image
        size = thumb_size
        if not thumb_size:
            rate = 0.2
            size = base.size
            size = (int(size[0] * rate), int(size[1] * rate))
        base.thumbnail(size)
        thumbnail = StringIO()
        base.save(thumbnail, 'PNG')
        thumbnail = ContentFile(thumbnail.getvalue())
        return thumbnail