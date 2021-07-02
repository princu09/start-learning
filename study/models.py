from django.db import models

# Custom User Create
from django.contrib.auth.models import AbstractUser

class UserManage(AbstractUser):
    userImg = models.FileField(null=True)
    fieldName = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    dob = models.DateField(null=True)

    class meta:
        ordering = ['last_name']

    def __str__(self):
        return self.fieldName