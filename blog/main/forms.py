from django import forms

class SignInForm(forms.Form):
    user_name = forms.CharField(label="User name", max_length=25)
    password = forms.CharField(label="Password", min_length=6, max_length=25,
        widget=forms.PasswordInput
    )

class SignUpForm(forms.Form):
    user_name = forms.CharField(label="User name", max_length=25)
    channel_name = forms.CharField(label="Channel name", max_length=25)
    password = forms.CharField(label="Password", min_length=6, max_length=25,
        widget=forms.PasswordInput
    )