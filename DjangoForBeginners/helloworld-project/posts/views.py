from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

class PostsPageView(ListView):
    model = Posts
    template_name = 'posts/posts.html'
