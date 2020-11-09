from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    곡물전분류 = models.CharField(max_length=10)
    김치류 = models.CharField(max_length=10)
    난류 = models.CharField(max_length=10)
    면류 = models.CharField(max_length=10)
    버섯류 = models.CharField(max_length=10)
    유제품 = models.CharField(max_length=10)
    육류 = models.CharField(max_length=10)
    조리가공품류 = models.CharField(max_length=10)
    채소류 = models.CharField(max_length=10)
    해산물 = models.CharField(max_length=10)
    기타 = models.CharField(max_length=10)
    조미료 = models.CharField(max_length=10)
    견과류 = models.CharField(max_length=10)


class foodmodel(models.Model):
    recipe_title = models.CharField(max_length=100) 
    raw_ingre = models.TextField()
    main_ingredients = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    method_type = models.TextField()
    cook_time = models.TextField()
    difficult = models.TextField()
    kcal = models.TextField()
    feature = models.TextField()
    raw_ingre_sep = models.TextField()

    def __str__(self):
        return f'{self.recipe_title}: {self.raw_ingre}'