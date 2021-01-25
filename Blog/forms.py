from django import forms
from .models import Article

class ModelForm(forms.ModelForm):
    model = Article
    class meta:
        fields = [
            'title',
            'content',
            'active',
        ]