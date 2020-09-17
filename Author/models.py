from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    username = models.CharField(max_length=50)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='author_avatar/')

    def __str__(self):
        return str(self.username).title().split(' ')[0]
