from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    mobile=models.CharField(max_length=15)
    concern=models.TextField(max_length=30)