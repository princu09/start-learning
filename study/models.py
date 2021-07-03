import datetime
from typing import Tuple
from django.db import models

# Custom User Create
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

class UserManage(AbstractUser):
    userImg = models.FileField(null=True)
    fieldName = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    dob = models.DateField(null=True)

    class meta:
        ordering = ['last_name']

    def __str__(self):
        return self.fieldName

subjects = (
    ('Gujarati','Gujarati'),
    ('Hindi', 'Hindi'),
    ('English','English'),
    ('Science','Science'),
    ('Mathematics','Mathematics'),
    ('Social Study' , 'Social-Study')
)
standard = (
    ('12' , 12),
    ('11' , 11),
    ('10' , 10),
    ('9' , 9),
    ('8' , 8),
    ('7' , 7),
    ('6' , 6),
    ('5' , 5)
)

class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    subject = models.CharField(choices=subjects , max_length=50)
    standard = models.CharField(choices=standard , max_length=50)
    presentation = models.FileField(upload_to="lacture/files_presentations")
    notes = models.FileField(upload_to="lacture/notes")
    video = models.FileField(upload_to="lacture/video")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"ID : {self.id} | Standard : {self.name} | Subject : {self.standard} | Name : {self.name}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=5000)
    chapter_id = models.IntegerField()

    def __str__(self):
        return f"Id : {self.id} | Comment : {self.comment}"