from django.urls import path
from .views import (
    home,
    form,
)
app_name = 'pages'  # for naming spacing for reverse url

urlpatterns = [
    path('', home),
    path('form/', form),
]