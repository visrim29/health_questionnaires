from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Response, Question
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return confirm_password


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responses'].required = False


class ResponseAdminForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].required = False