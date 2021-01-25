from django.db import models

# Create your models here.

class ToDo(models.Model):
    text=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_closed=models.BooleanField(default=False)
    is_favorite=models.BooleanField(default=False)
    
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.TextField(null=True)
    price=models.IntegerField(null=True)
    genre=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    year=models.DateField(null=True)
    date=models.DateField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)