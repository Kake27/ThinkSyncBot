from django import forms

class NameForm(forms.Form) :
    name = forms.CharField(label="name", max_length=100)
    company = forms.CharField(label="company", max_length=100)
    link = forms.CharField(label="link", max_length=100)