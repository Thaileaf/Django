from django.shortcuts import render
from .forms import RegularForm

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'pages/basic.html')

def form(request, *args, **kwargs):
    context = {
        'form': RegularForm(request.POST or None)
    }
    return render(request, 'pages/form.html', context)