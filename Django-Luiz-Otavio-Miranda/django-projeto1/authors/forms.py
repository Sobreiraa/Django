from django import forms 
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model= User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ] # Escolhendo os campos que desejamos

        #exclude = ['first_name']  Excluindo os campos que desejamos
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last name:',
            'username': 'Username:',
            'email': 'E-mail:',
            'password': 'Password:'
        }
        
        help_texts = {
            'email': 'The e-mail must be valid.'
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty.',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here.'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here.'
            })
        }