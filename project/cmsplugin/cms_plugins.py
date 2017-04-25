from cms.plugin_pool import plugin_pool
from .Children_view.children_view_plugin import OurChildrenPlugin

plugin_pool.register_plugin(OurChildrenPlugin)

