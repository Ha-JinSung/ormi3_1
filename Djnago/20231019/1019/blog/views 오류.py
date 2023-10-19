from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    
postlist = PostListView.as_view()
    
class PostCreatView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/form.html'
    
post_new = PostCreatView.as_view()

class PostDetailView(DeleteView):
    model = Post

post_detail = PostDetailView.as_view()

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/form.html'

post_edit = PostUpdateView.as_view()

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

post_delete = PostDeleteView.as_view()