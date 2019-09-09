from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role_id= models.IntegerField(default=0)

# Create your models here.
