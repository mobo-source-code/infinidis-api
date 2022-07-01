from django.shortcuts import render

from rest_framework import viewsets
from .models import OneDelivery, OneClient
from .serializers import ClientSerializer, DeliverySerializer


class AddDelivery(viewsets.ModelViewSet):

    queryset = OneDelivery.objects.all()
    serializer_class = DeliverySerializer


class ClientDelivery(viewsets.ModelViewSet):

    queryset = OneClient.objects.all()
    serializer_class = ClientSerializer



