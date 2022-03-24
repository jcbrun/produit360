from rest_framework import serializers
from produitApi.models import Barcode

class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ('id', 'barcode', 'itemKey', 'datetimeCreated', 'datetimeUpdated' )