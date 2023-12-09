from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user', 'first_name', 'middle_name', 'last_name', 'student_number', 'front_library_card', 'back_library_card']