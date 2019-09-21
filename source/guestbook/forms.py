from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, label='Name:')
    email = forms.EmailField(max_length=70, required=True, label='Email:')
    text = forms.CharField(max_length=1000, required=True, label='Text:',
                           widget=widgets.Textarea)