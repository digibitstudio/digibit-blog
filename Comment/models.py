from django.db import models

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    commentator = models.ForeignKey('Account.Account', null=True, on_delete=models.CASCADE, related_name='Comment')
    date = models.DateTimeField(verbose_name='Date Posted', auto_now_add=True)
    blog = models.ForeignKey('Blog.Post', on_delete=models.CASCADE, related_name='Comment')

    def __str__(self):
        extra = ''
        if len(self.comment) > 25:
            extra = '...'
        return f'{str(self.comment).title()[0:25]}{extra}'