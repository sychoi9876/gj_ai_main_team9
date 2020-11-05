from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    밥빵 = models.CharField(max_length=10)
    김치류 = models.CharField(max_length=10)
    난류 = models.CharField(max_length=10)
    면류 = models.CharField(max_length=10)
    버섯류 = models.CharField(max_length=10)
    유제품 = models.CharField(max_length=10)
    육류 = models.CharField(max_length=10)
    조리가공식품류 = models.CharField(max_length=10)
    채소류 = models.CharField(max_length=10)
    해산물 = models.CharField(max_length=10)
