from django.contrib import admin

# Register your models here.

from produitApi.models import Barcode

class BarcodeAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('id', 'barcode', 'itemKey', 'datetimeCreated', 'datetimeUpdated') # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Barcode, BarcodeAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
