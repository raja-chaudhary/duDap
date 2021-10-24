from django import forms
from django.forms import ModelForm

from .models import Promise


class PromiseForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.TextInput()
    deliver_by = forms.DateInput()

    class Meta:
        model = Promise
        fields = ['title', 'content', 'deliver_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Add new promise...'})
        self.fields['content'].widget.attrs.update(
            {
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Add promise context...'
            })
        self.fields['deliver_by'].widget.attrs.update(
            {
                'class': 'border border-purple-600 rounded w-full pl-4 pr-10 py-3 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Select date...'
            })
