from django.db import models

# Create your models here.

class TestType(models.Model):
    name = models.CharField(max_length=530)
    # price = models.CharField(max_length=50)
    description = models.CharField(max_length=1050)
    note = models.CharField(max_length=10000)
    interpretation = models.CharField(max_length=1110)
    # testdetails = models.ManyToManyField(TestDetail)
    
    def __str__(self):
        return self.name
    
class TestDetail(models.Model):
    testName = models.CharField(max_length=250)
    # results = models.CharField(max_length=10)
    units = models.CharField(max_length=50)
    bio_ref_interval = models.CharField(max_length=50)
    # lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    testType = models.OneToOneField(TestType, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    
    def __str__(self):
        return self.testName
     
# class TestType(models.Model):
#     name = models.CharField(max_length=530)
#     # price = models.CharField(max_length=50)
#     description = models.CharField(max_length=1050)
#     note = models.CharField(max_length=10000)
#     interpretation = models.CharField(max_length=1110)
#     # testdetails = models.ManyToManyField(TestDetail)
# class TestName(models.Model):
    
class Plan(models.Model):
    name = models.CharField( max_length=350)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=350)
    test = models.ManyToManyField(TestDetail)