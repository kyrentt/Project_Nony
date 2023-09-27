from django.db import models

# Create your models here.
class persona(models.Model):
    nombre=models.CharField(max_length=30)
    mail=models.EmailField()
    pas=models.CharField(max_length=10)
