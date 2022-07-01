from dataclasses import fields
import imp
from .models import OneDelivery, OneClient
from rest_framework import serializers

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = OneDelivery
        fields = '__all__'
        extra_kwargs = {"type_de_paiment" : {"required": False, "allow_null": True}, 
                        "status": {"required": False, "allow_null": True}}

    def to_representation(self, instance):
        rep = super(DeliverySerializer, self).to_representation(instance)
        rep['destinataire'] = instance.destinataire.nom
        return rep


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneClient
        fields = '__all__'