from django import forms
from django.forms import ModelForm

from .models import TRAIT_CHOICES, Trait


class TraitForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.TextInput()
    trait_type = forms.ChoiceField(
        label='Select The Trait Type', widget=forms.RadioSelect, choices=TRAIT_CHOICES)

    class Meta:
        model = Trait
        fields = ['title', 'content', 'trait_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add new trait...'})
        self.fields['content'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add trait context...'
            })
        self.fields['trait_type'].widget.attrs.update(
            {
                'class': 'text-gray-600 text-3xl h-3 w-3 text-red-600',
            })
