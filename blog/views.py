from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


class PostListView(ListView):
    """Displays a list of  posts on the main page"""

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# TODO: Replacing a function with class
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


def post_share(request, post_id):
    """
    Sharing post.
    :param request:
    :param post_id: post's id
    :return:
    """
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd.name}'s comments: {cd['comments']}"
            send_mail(subject, message, 'amstl86@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'form': form,
                                                    'post': post,
                                                    'sent': sent})


@require_POST
def post_comment(request, post_id):
    """
    Adding a comment to a post.
    :param request:
    :param post_id: id the post
    :return:
    """
    post = get_object_or_404(Post, pk=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})
