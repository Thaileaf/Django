from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'home.html', {})

def contact_view(request,*args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [123, 345, 567, 'abc'],
        'is_true': True,
        'title': 'fugedabouit',
        'title2': 'Seriously',
        'my_html': '<p>My html<p>'
    }
    return render(request, 'contact.html', my_context)

def extend(request, *args, **kwargs):
    return render(request, 'extend.html', {})