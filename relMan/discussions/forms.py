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
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Add new argument...'})
        self.fields['content'].widget.attrs.update(
            {
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
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
