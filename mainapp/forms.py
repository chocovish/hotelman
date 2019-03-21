from django import forms
from .models import Invoice
class InvoiceForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    room_no = forms.CharField(widget=forms.TextInput(attrs={'list':'rooms'}))

    check_in_2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    check_out_2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    room_no_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'list':'rooms'}))
    rate_2 = forms.IntegerField(required=False)
    days_count_2 = forms.IntegerField(required=False)

    check_in_3 = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    check_out_3 = forms.DateField(required=False, widget=forms.DateInput(attrs={'type':'date'}))
    room_no_3 = forms.CharField(required=False, widget=forms.TextInput(attrs={'list':'rooms'}))
    rate_3 = forms.IntegerField(required=False)
    days_count_3 = forms.IntegerField(required=False)

    class Meta:
        model = Invoice
        exclude = []

class SearchByDateForm(forms.Form):
    tdate = forms.DateField()
    fdate = forms.DateField()