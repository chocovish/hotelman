from django import forms
from .models import Invoice
class InvoiceForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check_in = forms.DateField(label="Room In", widget=forms.DateInput(attrs={'type':'date'}))
    check_out = forms.DateField(label="Room Out", widget=forms.DateInput(attrs={'type':'date'}))
    room_no = forms.CharField(widget=forms.TextInput(attrs={'list':'rooms'}))

    check_in_2 = forms.DateField(label="Room In 2", required=False, widget=forms.DateInput(attrs={'type':'date'}))
    check_out_2 = forms.DateField(label="Room Out 2", required=False, widget=forms.DateInput(attrs={'type':'date'}))
    room_no_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'list':'rooms'}))
    
    check_in_3 = forms.DateField(label="Room In 3", required=False, widget=forms.DateInput(attrs={'type':'date'}))
    check_out_3 = forms.DateField(label="Room Out 3", required=False, widget=forms.DateInput(attrs={'type':'date'}))
    room_no_3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'list':'rooms'}))

    class Meta:
        model = Invoice
        exclude = []

class SearchByDateForm(forms.Form):
    tdate = forms.DateField()
    fdate = forms.DateField()