from django import forms
from django.forms import ModelForm

from .models import Discussion


class DiscussionForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.TextInput()

    class Meta:
        model = Discussion
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add new argument...'})
        self.fields['content'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Add argument context...'
            })

    # def __init__(self, *args, **kwargs):
    #     super(DiscussionForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({
    #         'class': 'appearance-none placeholder-gray-800 bg-transparent w-full my-4 text-gray-700 py-0 px-2 leading-normal focus:outline-none text-sm sm:text-lg border-b-2 border-gray-800',
    #         'placeholder': 'Add Argument Title'
    #     })
    #     self.fields['content'].widget.attrs.update({
    #         'class': 'appearance-none placeholder-gray-800 bg-transparent w-full my-4 text-gray-700 py-0 px-2 leading-normal focus:outline-none text-sm sm:text-lg border-b-2 border-gray-800',
    #         'placeholder': 'Add Argument Content'
    #     })
