from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """
    Displays a list of posts on the main page
    :return: all posts
    """
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    """
    Displays the selected post
    :param request:
    :param id: post id
    :return: selected post
    """
    post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
