
from ..models import Post

def get_all_posts():
    return Post.objects.all()

def get_all_post_for_user(self, user):
    try:
        return Post.objects.filter(User=user)
    except:
        pass


