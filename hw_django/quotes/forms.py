from django import forms
from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quote, Tag

class AuthorForm(forms.ModelForm):
    fullname=CharField(min_length=1, max_length=150, required=True, widget=TextInput())
    born_date=CharField(min_length=1, max_length=150, required=True, widget=TextInput())
    born_location=CharField(min_length=1, max_length=150, required=True, widget=TextInput())
    description=CharField(min_length=1, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    quote = CharField(min_length=10, max_length=150, required=True, widget=TextInput())
    # author = CharField(min_length=10, max_length=150, required=True, widget=TextInput())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None)
    # tags = CharField(min_length=1, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        # exclude = ['tags']