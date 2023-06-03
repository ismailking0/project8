from django.db import models

# Create your models here
class RegView(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    email=models.EmailField()
    mobno=models.IntegerField()

