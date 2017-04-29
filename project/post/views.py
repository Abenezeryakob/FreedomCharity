from django.shortcuts import get_object_or_404, render,redirect

from .models import Post

# Create your views here.

def post_view(request,slug):

    post = get_object_or_404(Post,slug=slug)
    return render(request, 'post_list.html', {
        'post': post,
    })


def post_list_view(request):
    post = Post.objects.all()
    return (
        render(request, 'post_list.html',{'post':post} )
    )


