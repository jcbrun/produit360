from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from produitApi.models import Barcode
from produitApi.serializers import BarcodeSerializer

# Create your views here.

@csrf_exempt
def barcodeApi(request, id=0):
    if request.method == 'GET':
        barcodes = Barcode.objects.all()
        barcodeSerializer = BarcodeSerializer(barcodes, many=True)
        return JsonResponse(barcodeSerializer.data, safe=False)
    elif request.method == 'POST':
        barcodeData = JSONParser().parse(request)
        barcodeSerializer = BarcodeSerializer(data=barcodeData)
        if barcodeSerializer.is_valid():
            barcodeSerializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add : "+str(barcodeSerializer.errors), safe=False)
    elif request.method == 'PUT':
        barcodeData = JSONParser().parse(request)
        barcode = Barcode.objects.get(id=id)
        print(id," -- ",barcodeData)
        barcodeSerializer = BarcodeSerializer(barcode, data=barcodeData)
        if barcodeSerializer.is_valid():
            barcodeSerializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update : ", safe=False)
    elif request.method == 'DELETE':
        barcode = Barcode.objects.get(id=id)
        barcode.delete()
        return JsonResponse("Delete Successfully", safe=False)