from django import forms
from django.forms import ModelForm

from .models import REMINDER_CHOICES, Date


class DateForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    date = forms.DateInput()
    reminder = forms.ChoiceField(choices=REMINDER_CHOICES)

    class Meta:
        model = Date
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-md',
                'placeholder': 'Title for occassion...'})
        self.fields['date'].widget.attrs.update(
            {
                'class': 'w-full pl-4 pr-10 py-3 leading-none rounded-lg shadow-sm focus:outline-none text-gray-600 font-medium focus:ring focus:ring-blue-600 focus:ring-opacity-50',
                'placeholder': 'Select date...'
            })
        self.fields['reminder'].widget.attrs.update(
            {
                'class': 'w-full pl-4 pr-10 py-3 leading-none rounded-lg shadow-sm focus:outline-none text-gray-600 font-medium focus:ring focus:ring-blue-600 focus:ring-opacity-50',
                'placeholder': 'Remind In...',
                'default': 'One Week Prior'
            })
