from django import forms
# from .models import Bornapp

# class ModelBornForm(forms.ModelForm):
#     class Meta:
#         model = Bornapp
#         fields = [
#             'title',
#             'description',
#             'choices',
#         ]
#
#     def clean_title(self, *args, **kwargs):
#         title = self.cleaned_data.get('title')
#         if 'bruh' not in title:
#             raise forms.ValidationError('bruh')
#         else:
#             return title
#
# class RawBornForm(forms.Form):
#     title = forms.CharField(label='click here if dumb', widget=forms.Textarea(attrs={'rows': 5, 'placeholder':'hahahahahahaaa'}))
#     description = forms.CharField(required=False)
#     choices = forms.ChoiceField(choices=[
#         ('gay', 'Gay'),
#         ('notgay', 'Not Gay'),
#     ])