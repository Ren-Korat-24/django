from django.db import models

# Create your models here.
class Homehtml(models.Model):
    name =models.CharField(max_length=30,default='')
    email =models.CharField(max_length=50,default='')