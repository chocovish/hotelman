from django import forms
from .models import Invoice
class InvoiceForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    room_no = forms.CharField(widget=forms.TextInput(attrs={'list':'rooms'}))
    class Meta:
        model = Invoice
        exclude = []

class SearchByDateForm(forms.Form):
    tdate = forms.DateField()
    fdate = forms.DateField()