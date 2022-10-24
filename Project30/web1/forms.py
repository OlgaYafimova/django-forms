from django import forms

class MyForm(forms.Form):
    surname = forms.CharField(max_length=25)
    name = forms.CharField(max_length=25)
    age = forms.IntegerField()
