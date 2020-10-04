from django.db import models
from django.utils.text import slugify

class Topic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return str(self.topic).title()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    author = models.ForeignKey('Author.Author', related_name='post', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Date Posted', auto_now_add=True)
    view = models.SmallIntegerField(null=True)
    upvote = models.SmallIntegerField(null=True)
    topic = models.ManyToManyField(Topic, related_name='Post')
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title).title()

