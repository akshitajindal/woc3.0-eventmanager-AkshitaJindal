from django.db import models
from django import forms

# Create your models here.

class eventRegistration(models.Model):
    eventName = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    posterLink = models.URLField(max_length=200, default='NULL')
    fromDate = models.DateTimeField()
    toDate = models.DateTimeField()
    registrationDeadline = models.DateTimeField()
    hostEmail = models.EmailField()
    hostPassword = models.CharField(max_length=50)

class participantRegistration(models.Model):
    participantName = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=12)
    participantEmail = models.EmailField()
    eventName = models.CharField(max_length=50)
    eventId = models.PositiveIntegerField(default=0)
    registrationType = models.CharField(max_length=50)
    noOfPeople = models.PositiveIntegerField()