from rest_framework.serializers import ModelSerializer

from core.models import TuristicPoint


class TuristicPointSerializer(ModelSerializer):
    class Meta:
        model = TuristicPoint
        fields = ['id', 'name', 'description', 'approved', 'picture']
