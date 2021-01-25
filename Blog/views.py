from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

# Create your views here.
# def list_view(request, *arg, **kwargs):
    # articles = Article.objects.all()
    # context = {
    #     'articles': articles
    # }
    # return render(request, 'Blog/article_list.html', context)

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')