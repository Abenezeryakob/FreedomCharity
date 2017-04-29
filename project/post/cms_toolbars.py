from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from post.models import Post


class PostToolbar(CMSToolbar):
    supported_apps = (
        'Post',
    )

    watch_models = [Post]

    def populate(self):
        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('post-app', _('Post'))

        menu.add_sideframe_item(
            name=_('Post list'),
            url=admin_reverse('posts_post_changelist'),
        )

        menu.add_modal_item(
            name=_('Add new Post'),
            url=admin_reverse('posts_post_add'),
        )


toolbar_pool.register(PostToolbar)