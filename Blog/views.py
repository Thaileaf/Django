from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView)

# Create your views here.
# def list_view(request, *arg, **kwargs):
    # articles = Article.objects.all()
    # context = {
    #     'articles': articles
    # }
    # return render(request, 'Blog/article_list.html', context)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title, content']


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About',

                                               })

