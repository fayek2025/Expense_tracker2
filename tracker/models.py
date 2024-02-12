from django.db import models

# Create your models here.

class record(models.Model):
    Name = models.CharField(max_length=50)
    Expenses = models.IntegerField()
    Created_at = models.DateTimeField( auto_now_add= True)
    