from django import forms
from Blog.models import Post
from djrichtextfield.widgets import RichTextWidget

class CreatePostForm(forms.ModelForm):
    body = forms.CharField(widget=RichTextWidget)
    class Meta:
        model = Post
        fields = ('title', 'topic', 'body')