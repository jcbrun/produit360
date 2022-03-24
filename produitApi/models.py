
from django.db import models

# Create your models here.

class Barcode(models.Model):
    id = models.AutoField(primary_key=True)
    barcode = models.CharField(max_length=13, unique=True)
    itemKey = models.IntegerField(default=0)
    datetimeCreated = models.DateTimeField(auto_now_add=True)
    datetimeUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):          # Est utiliser pour printer simplement l'objet
        return self.barcode
