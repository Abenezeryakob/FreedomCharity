from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PostAppHook(CMSApp):
    name = _('post')
    app_name = "post"

    def get_urls(self, page=None, language=None, **kwargs):
        return ['post.urls']

apphook_pool.register(PostAppHook)