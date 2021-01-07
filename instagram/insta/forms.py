from .models import Profile
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            helper.form_show_labels= False

   