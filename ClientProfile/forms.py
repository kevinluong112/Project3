from django import forms

class ClientProfileForm(forms.Form):
    name = forms.CharField (label = 'Full Name', max_length=255)
    description = forms.CharField (label = 'Description', max_length=255)
    price = forms.DecimalField(label= 'Price')
    history = forms.CharField (label = 'History', max_length=255)
    summary = forms.CharField (label = 'Summary', max_length=255)