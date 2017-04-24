from .childern_view_model import SelectOurChildren
from cms.plugin_base import CMSPluginBase

class OurChildrenPlugin(CMSPluginBase):
    model = SelectOurChildren
    name = 'Top - OurChildren'
    render_template = 'cmsplugin/top_children/top_children.html'

    def render(self, context, instance, placeholder):
        request = context['request']

        context.update({
            'instance': instance,
        })

        print( instance.our_children)
        for i in instance.our_children.all():
            print(i.first_name)
        return context