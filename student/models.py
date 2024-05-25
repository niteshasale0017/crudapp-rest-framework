from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)

