from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return str(self.topic).title()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    author = models.ForeignKey('Account.Account', related_name='post', on_delete=models.SET_NULL, null=True)
    date = models.DateField(verbose_name='Date Posted', auto_now_add=True)
    view = models.SmallIntegerField(null=True)
    upvote = models.SmallIntegerField(null=True)
    topic = models.ManyToManyField(Topic, related_name='Post')

    def __str__(self):
        return str(self.title).title()

