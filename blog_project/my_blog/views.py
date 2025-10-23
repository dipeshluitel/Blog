from django.shortcuts import render
from django.utils import timezone
from my_blog.forms import PostForm, CommentForm
from my_blog.models import Post,Comment
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # in place of decorators for CBV
from django.views.generic import (TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'my_blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'my_blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')