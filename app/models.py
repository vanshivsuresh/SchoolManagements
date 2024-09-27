from django.db import models

# Create your models here.

class SchoolManagements(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Heroku_External_ID = models.IntegerField(default=1)

    def __str__(self):
        return self.name



class VanshivManagements(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

