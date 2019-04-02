from django import forms

class TodoInputForm(forms.Form):
    date = forms.DateField()
    content = forms.CharField()