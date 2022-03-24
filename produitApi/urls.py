
#from django.conf.urls import url
from django.urls import re_path as url
from produitApi import views


urlpatterns = [
    url(r'^barcode$', views.barcodeApi),
    url(r'^barcode/([0-9]+)$', views.barcodeApi)
]

