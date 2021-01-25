"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [

    path('products/', include('products.urls')),  # include() just tags the product.urls onto the products/ app
    path('bornapp/', include('bornapp.urls')),
    path('pages/', include('pages.urls')),
    path('blog/', include('Blog.urls')),


    path('admin/', admin.site.urls, name='blah'), # Name is getting absolute url through reverse in models

]
