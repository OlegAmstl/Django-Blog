from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """
    Displays a list of posts on the main page
    :return: all posts
    """
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    """
    Displays the selected post
    :param request:
    :param year: year the post was published
    :param month: month the post was published
    :param day: day the post was published
    :param post: slug the post
    :return: selected the post
    """
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})
