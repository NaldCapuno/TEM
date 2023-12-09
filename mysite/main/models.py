from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, null=True)
    student_number = models.CharField(max_length=11, unique=True, null=True)
    email = models.EmailField(null=True)
    front_library_card = models.ImageField('Front side of your library card:', upload_to='images/', null=True)
    back_library_card = models.ImageField('Back side of your library card:', upload_to='images/', null=True)

    def __str__(self):
        return self.student_number