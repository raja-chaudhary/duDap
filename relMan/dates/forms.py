from django import forms
from django.forms import ModelForm

from .models import REMINDER_CHOICES, Date


class DateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    date = forms.DateInput()
    reminder = forms.ChoiceField(choices=REMINDER_CHOICES)

    class Meta:
        model = Date
        fields = ['title', 'date', 'reminder']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'border rounded w-full py-2 px-4 text-purple-500 shadow-sm leading-none focus:outline-none focus:ring focus:ring-purple-600 focus:ring-opacity-50 placeholder-purple-500 bg-purple-50',
                'placeholder': 'Title for occassion...'})
        self.fields['date'].widget.attrs.update(
            {
                'class': 'w-full pl-4 pr-10 py-2 leading-none rounded shadow-sm focus:outline-none text-purple-500 focus:ring focus:ring-purple-600 focus:ring-opacity-50 bg-purple-50',
                'placeholder': 'Select date...'
            })
        self.fields['reminder'].widget.attrs.update(
            {
                'class': 'w-full px-4 py-2 leading-none rounded shadow-sm focus:outline-none text-purple-500 focus:ring focus:ring-purple-600 focus:ring-opacity-50 bg-purple-50',
                'placeholder': 'Remind In...',
                'default': 'One Week Prior'
            })
