from django.db import models


from django.db import models

class Recruiter(models.Model):
    username = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    
    age = models.IntegerField()
    dob = models.DateField()
    companyName=models.CharField(max_length=100)
    designationName=models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contactNumber = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmPassword = models.CharField(max_length=100)
    image=models.ImageField(upload_to="image")

class Parser(models.Model):
   
    file=models.FileField(upload_to="image")
