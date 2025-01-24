from django import forms    
from django.contrib.auth import forms
from .models import Users

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users
        fields = ('email', 'name', 'is_active', 'is_staff')

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users
        fields = ('email', 'name', 'password1', 'password2')