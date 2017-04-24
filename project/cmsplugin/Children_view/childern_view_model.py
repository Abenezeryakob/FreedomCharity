from cms.models import CMSPlugin
from django.db import models
from our_children.models import OurChildren

class SelectOurChildren(CMSPlugin):
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    our_children = models.ManyToManyField(OurChildren)

    def copy_relations(self, old_instance):
        self.our_children = old_instance.our_children.all()

    def get_data(self):
        return (self.our_children.objects.all())