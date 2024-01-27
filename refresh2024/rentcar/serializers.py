from rest_framework import serializers

from .models import Elan

from .models import Car

class ElanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elan
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
