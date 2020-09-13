from django import forms

class To_enter(forms.Form):
    username = forms.CharField(
        max_length=100, min_length=5, label='Username', required=True)
    password = forms.CharField(
        max_length=25, min_length=8, widget=forms.PasswordInput, required=True)
