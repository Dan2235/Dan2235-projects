from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(
        label="Эл. почта",
        widget=forms.EmailInput
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )

class AccountForm(forms.Form):
    email = forms.EmailField(
        label="Эл. почта",
        widget=forms.EmailInput
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
    name = forms.CharField(
        label="Имя",
        max_length=20,
        min_length=2,
        widget=forms.TextInput
    )
    age = forms.IntegerField(
        label="Возраст",
        max_value=100,
        min_value=1,
        widget=forms.NumberInput
    )