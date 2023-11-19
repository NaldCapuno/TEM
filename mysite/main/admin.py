from django.contrib import admin
from .models import UserInfo

# Register your models here.
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_initial', 'last_name', 'student_number']
    search_fields = ['first_name', 'middle_initial', 'last_name', 'student_number']