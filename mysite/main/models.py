from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    student_number = models.CharField(max_length=11, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student Number: {self.student_number}\nName: {self.first_name} {self.middle_name} {self.last_name}"