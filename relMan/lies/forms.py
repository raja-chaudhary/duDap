from django import forms
from django.forms import ModelForm

from .models import Lie


class LieForm(forms.ModelForm):
    title = forms.CharField(max_length=500)

    class Meta:
        model = Lie
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'They dare lie...??'})
