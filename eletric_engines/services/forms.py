from django import forms
from .models import Services

class Record(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['address', 'stret', 'number', 'zipe_code', 'reference', 'request_date']

    address = forms.CharField(max_length=32, min_length=5, required=True)
    stret = forms.CharField(max_length=150, min_length=5, required=False)
    number = forms.IntegerField(required=False)
    zipe_code = forms.CharField(max_length=8, min_length=8,required=False)
    reference = forms.CharField(max_length=150,required=False)
    request_date = forms.DateField(required=True)

class Update(forms.ModelForm):
    request_date = forms.DateField(required=True)