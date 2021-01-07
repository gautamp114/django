from django import forms
from .models import UserRegistration

# class UserLoginForm(forms.ModelForm):
#     username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Place in the username'}))
#     password = forms.PasswordField(widget= forms.PasswordInput(attrs={'class':'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Place in the username'}))
    email = forms.EmailField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Place in the email'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = UserRegistration
        fields = ['username ', 'password', 'email']
