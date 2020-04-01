from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django.contrib.auth.forms import PasswordResetForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter name', 'class': 'input_textinput'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter new email', 'class': 'input_textinput'}),

        }

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Смена ника'
        self.fields['username'].hilp_text = 'Смена почты'
        self.fields['email'].label = 'Смена почты'




class ProfileUpdateForm(forms.ModelForm):
    images = forms.ImageField(label='')

    class Meta:

        model = UserProfile
        fields = ['images']

