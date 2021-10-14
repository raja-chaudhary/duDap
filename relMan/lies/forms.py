from django import forms
from django.forms import ModelForm

from .models import Lie


class LieForm(forms.ModelForm):
    title = forms.CharField(max_length=500)

    class Meta:
        model = Lie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'They dare lie...??'})
