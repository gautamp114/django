from django import forms
from .models import CustomerLogin
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Place in the username'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Place in the email'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Email must be gmail.com")
        return email


class CustomerMoreForm(forms.ModelForm):
    class Meta:
        model = CustomerLogin
        fields = ['address']

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Place in the username'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'password')
