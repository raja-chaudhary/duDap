from django import forms
from django.forms import ModelForm

from .models import Sex


class SexForm(forms.ModelForm):
    sex_count = forms.IntegerField()

    class Meta:
        model = Sex
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sex_count'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add new promise...'})
