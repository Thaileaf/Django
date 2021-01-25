from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import ProductForm, RawProductForm

# def product_create_view(request):
#
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#             print(Product.objects.all())
#         else:
#             print(form.errors)
#         print('hello')
#     context = {
#         'form': form
#     }
#     return render(request, 'products/product_create.html', context)

# Create your views here.
def product_create_view(request, *args, **kwargs):
    initial_data = {
        'title': 'My awesome Title'
    }
    obj = Product.objects.get(id=1)
    # Setting obj to instance of form to edit data. Initial data is just initial
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form':form
    }
    return render(request, 'products/product_create.html', context)



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

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object':obj
    }
    return render(request, 'products/product_detail.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object':obj
    }
    return render(request, 'products/product_delete.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)