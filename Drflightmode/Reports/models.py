from django.db import models

from TestDetails.models import *
from UserDetails.models import *
# Create your models here.

class PatientTestDetail(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    result = models.CharField(max_length=50)
    parameter = models.ForeignKey(TestDetail, on_delete=models.CASCADE)
    dateTimeCollection = models.DateTimeField(auto_now=False, auto_now_add=True)
    dateTimeReceived = models.DateTimeField(auto_now=True, auto_now_add=False)
    dateTimeReported = models.DateTimeField(auto_now=False, auto_now_add=False)