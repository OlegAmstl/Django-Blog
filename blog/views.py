from django.shortcuts import render
from .models import Post


def post_list(request):
    """
    Displays a list of posts on the main page
    :param request:
    :return: all posts
    """
    posts = Post.publish.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
