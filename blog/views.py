from pathlib import Path
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post, Comment, Author
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse



class HomepageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date']
    context_object_name = 'latest_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = ['-date']
    context_object_name = 'all_posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post-form.html'
    fields = ['title', 'slug', 'author', 'image', 'excerpt', 'content']

    def get_success_url(self):
        return reverse('post-detail-page', kwargs={'slug': self.object.slug})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post-form.html'
    fields = ['title', 'slug', 'author', 'image', 'excerpt', 'content']

    def get_success_url(self):
        return reverse('post-detail-page', kwargs={'slug': self.object.slug})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post-confirm-delete.html'
    success_url = reverse_lazy('posts-page')

def homepage(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {'latest_posts': latest_posts}) 


def posts(request):  
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/index.html', {"all_posts": all_posts})


class PostDetail:
    def __init__(self, title, content, author, created_at, image):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at
        self.image = image

    def __str__(self):
        return self.title
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'post/post-detail.html', {'post': identified_post})

def error_404_view(request, exception):
    return render(request, '404.html')