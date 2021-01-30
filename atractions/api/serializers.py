from rest_framework.serializers import ModelSerializer
from atractions.models import Atraction


class AttractionsSerializer(ModelSerializer):
    class Meta:
        model = Atraction
        fields = ['id','name', 'description', 'opening_hours', 'minimum_age']