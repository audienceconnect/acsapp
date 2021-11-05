from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.


BLOOD_GROUP = [
    ('A', 'A'),
    ('A+', 'A+'),
    ('B-', 'B-'),
    ('B+', 'B+'),
    ('AB', 'AB'),
    ('O-', 'O-'),
    ('O+', 'O+'),
]

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.name

class Patient(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True),
    blank = (True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP)

    def  __str__(self):
        return self.users.username


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True),
    blank = (True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP)
    experience = models.CharField(max_length=250, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER)

    def  __str__(self):
        return self.users.username

  
        

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    a_date = models.DateTimeField(null=True)

    def  __str__(self):
        return self.doctor.user.username+ " "+self.patient.user.username
    