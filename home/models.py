from django.db import models

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email =  models.EmailField()
    addres = models.TextField(null=True , blank = True)
    file = models.FileField()
    