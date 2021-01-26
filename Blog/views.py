from django.shortcuts import render

posts = [
    {
        'author': 'Thaison',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'Person2',
        'title': 'Blog Post 2',
        'content': 'SEcond post content',
        'date_posted': 'August 28, 2018',
    }

]
from .models import Article

# Create your views here.
# def list_view(request, *arg, **kwargs):
    # articles = Article.objects.all()
    # context = {
    #     'articles': articles
    # }
    # return render(request, 'Blog/article_list.html', context)

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'Blog/home.html', context)

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About',

                                               })