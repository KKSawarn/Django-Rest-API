from django.db import models
from django.db.models import fields
from passenger.models import Passenger
from rest_framework import serializers

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','firstName','lastName','travelPoints']
