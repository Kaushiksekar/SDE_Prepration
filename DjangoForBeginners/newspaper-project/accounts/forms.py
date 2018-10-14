from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields
        fields = ('username', 'email',) # don't need to add password as its mandatory

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email',)
