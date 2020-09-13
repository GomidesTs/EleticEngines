from django import forms
from .models import Services

class Record(forms.Form):
    class Meta:
        model = Services
        filds = ['address', 'stret', 'number', 'zipe_code', 'reference']

    
    address = forms.CharField(max_length=32, min_length=5, required=True)
    stret = forms.CharField(max_length=150, min_length=5, required=False)
    number = forms.ImageField(max_length=5,required=False)
    zipe_code = forms.CharField(max_length=8, min_length=8,required=False)
    reference = forms.CharField(max_length=150,required=False)
