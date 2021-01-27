from django.shortcuts import render
from .models import Post

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

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About',

                                               })