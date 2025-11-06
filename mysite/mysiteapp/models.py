from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    # cpassword = models.CharField(max_length=25)