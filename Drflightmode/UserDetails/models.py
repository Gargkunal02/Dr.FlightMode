from django.db import models

from django.contrib.auth.models import AbstractUser

from TestDetails.models import Plan

# Create your models here.


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    # gender = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=10)
    secondaryPhoneNumber = models.CharField(max_length=10)
    email= models.CharField(max_length=250)
    address = models.TextField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.first_name

class Lab(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ManyToManyField(Doctor)
    plan = models.ManyToManyField(Plan)
    
    def __str__(self):
        return self.user.first_name
