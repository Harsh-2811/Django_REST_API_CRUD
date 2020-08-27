from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=20)
    Email=models.CharField(max_length=40)
    Mobile_No=models.CharField(max_length=10)
    Department=models.CharField(max_length=10)

    def __str__(self):
        return  self.Name