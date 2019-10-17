from django import forms
from luminus.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        filter_result = User.objects.using('luminus').filter(uname=username).exists()
        if not filter_result:
            raise forms.ValidationError("This username does not exist. Please register first.")

        return username
