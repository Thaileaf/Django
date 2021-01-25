from django import forms

class ModelForm(forms.ModelForm):
    class meta:
        # model = INsert model
        fields = [
            'description'
            'help'
            'idk'
        ]

    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data('description')
        if 'cfe' not in description:
            raise forms.ValidationError('Cant do that bitch')
        else:
            return description


class RegularForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':20}))