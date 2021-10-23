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
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Add new trait...'})
        self.fields['content'].widget.attrs.update(
            {
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Add trait context...'
            })
        self.fields['trait_type'].widget.attrs.update(
            {
                'class': 'text-purple-600 ',
            })
