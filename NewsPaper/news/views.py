from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = 'post_title'
    template_name = 'flatpages/post.html'
    context_object_name = 'post'

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news.html'
