from rest_framework import serializers
from .models import HojaVida

class HojaVidaSerializer (serializers.ModelSerializer):
    class Meta:
        model = HojaVida
        fields = "__all__"