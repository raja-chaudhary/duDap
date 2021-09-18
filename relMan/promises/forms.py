from django import forms
from django.forms import ModelForm

from .models import Promise


class PromiseForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.TextInput()
    deliver_by = forms.DateInput()

    class Meta:
        model = Promise
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add new promise...'})
        self.fields['content'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add promise context...'
            })
        # self.fields['deliver_by'].widget.attrs.update(
        #     {
        #         'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md',
        #         'placeholder': 'Add promise context...'
        #     })
