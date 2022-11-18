from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HealthInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(blank = True, max_length = 6, null=True)

def __str__(self):
    return self.user.username



