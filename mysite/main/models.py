from django.db import models

# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    student_number = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f"Student Number: {self.student_number}\nName: {self.first_name} {self.middle_initial} {self.last_name}"