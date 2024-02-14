from django.db import models
import uuid
# Create your models here.

class record(models.Model):
    
    Name = models.CharField(max_length=50)
    Expenses = models.IntegerField()
    Created_at = models.DateTimeField( auto_now_add= True)
    
    
    def __str__(self):
        return (f"{self.Name} {self.Expenses} {self.Created_at}")
    