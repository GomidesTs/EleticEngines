from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Record(UserCreationForm, forms.Form):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    first_name = forms.CharField(max_length=20, min_length=3,required=True)
    last_name = forms.CharField(max_length=20, min_length=3,required=True),
    email = forms.EmailField(max_length=150, min_length=5, required=True)


class UpdateGrup(UserCreationForm, forms.Form):
    first_name = forms.CharField(max_length=20, min_length=3,required=True)
    last_name = forms.CharField(max_length=20, min_length=3,required=True)
    email = forms.EmailField(max_length=150, min_length=5, required=True)
