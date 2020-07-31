from django.shortcuts import render

from .models import Product

from .forms import ProductForm, RawProductForm

def product_create_view(request):

    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
            print(Product.objects.all())
        else:
            print(form.errors)
        print('hello')
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

# Create your views here.
# def product_create_view(request, *args, **kwargs):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form':form
#     }
#     return render(request, 'products/product_create.html', context)



def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object':obj
    }
    return render(request, 'products/product_detail.html', context)
