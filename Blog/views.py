from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from Blog.models import Post
from Blog.forms import CreatePostForm
from Author.models import Author
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ListPost(ListView):
    model = Post
    template_name = 'blog/list-post.html'

class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail-post.html'

class CreatePost(CreateView):
    model = Post
    template_name = 'blog/create-post.html'
    form_class = CreatePostForm
    success_url = 'post-list'
    
    def form_valid(self, form):
        obj = form.save(commit=False)        
        user = User.objects.get(email=self.request.user.email)
        if user.is_superuser or user.is_staff:
            try:
                author = Author.objects.get(user=user)
                obj.author = author
                obj.save()
            except ObjectDoesNotExistt:
                pass
        return redirect('list-post')

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete-post.html'    

    def get_success_url(self):
        return reverse('list-post')