from django.db import models

# Create your models here.
class adde(models.Model):
    mname= models.CharField(max_length=100)
    mabout= models.CharField(max_length=100)
    mstory= models.CharField(max_length=200)
    mcharge=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    mtime= models.TimeField((""), auto_now=False, auto_now_add=False)


class reserves(models.Model):
    name= models.CharField(max_length=100)
    name1= models.CharField(max_length=100)
    email1= models.EmailField()
    theater= models.CharField(max_length=25,blank=False,null=False)
    showdate= models.DateField()
    time1= models.TimeField((""), auto_now=False, auto_now_add=False)
    quantity= models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)


class Solve(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    subject= models.CharField(max_length=200)
    mess= models.CharField(max_length=200)
