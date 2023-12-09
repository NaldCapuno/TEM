from django.contrib import admin
from .models import UserInfo

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'middle_name', 'last_name', 'student_number', 'front_library_card', 'back_library_card']
    search_fields = ['user', 'student_number']