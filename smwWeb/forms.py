from django import forms

# Create your forms here.

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SigninForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_nd = forms.CharField(label="Password again", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")

class SettingsFileForm(forms.Form):
    settings = forms.FileField(label='Upload settings file')
