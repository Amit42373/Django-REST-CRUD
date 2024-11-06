# from django import forms

class Companyform(forms.Form):
    company_name = forms.CharField()
    location = forms.CharField()

