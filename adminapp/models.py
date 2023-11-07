from django.db import models

class Supervisor(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    aadhar=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    isactive=models.IntegerField()
    createdby=models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Drivers(models.Model):
    name=models.CharField(max_length=100)
    aadhar=models.CharField(max_length=100, null=True)
    licience=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    shift=models.CharField(max_length=100)
    drivertype=models.CharField(max_length=100)
    isactive=models.IntegerField()
    createdby=models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Cleaners(models.Model):
    name=models.CharField(max_length=100)
    aadhar=models.CharField(max_length=100, null=True)
    licience=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    shift=models.CharField(max_length=100)
    isactive=models.IntegerField()
    createdby=models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
