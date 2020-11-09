from django.contrib import admin
from .models import User

# Register your models here.

admin.site.register(User)

from .models import foodmodel

admin.site.register(foodmodel)