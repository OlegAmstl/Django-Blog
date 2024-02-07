from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """Manager for published posts."""

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Модель поста."""

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250,
                             verbose_name='Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор поста',
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата обновления')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                             self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
