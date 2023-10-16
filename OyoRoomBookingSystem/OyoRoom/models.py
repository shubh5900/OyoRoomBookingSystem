from django.db import models


from django.urls import reverse

class Customer(models.Model):
    roll=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=10)
    Address=models.CharField(max_length=200)
    

    # Create your models here.

    


