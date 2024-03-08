from rest_framework import serializers
from .models import Ofertas


class OfertaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Ofertas
        fields = "__all__"

