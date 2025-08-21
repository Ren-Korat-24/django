from django.db import models

# Create your models here.
class Homedata(models.Model):
    rollno =models.IntegerField(default='',max_length=3,unique=True)
    name = models.CharField(max_length=50,default='')
    hindi =models.IntegerField(max_length=3,default='')
    gujarati =models.IntegerField(max_length=3,default='')
    ss =models.IntegerField(max_length=3,default='')
    total =models.IntegerField(max_length=3,default='')
    min_marks =models.IntegerField(max_length=3,default='')
    max_marks =models.IntegerField(max_length=3,default='')
    percentage =models.FloatField(max_length=5,default='')
    grade =models.CharField(max_length=2,default='')
    
