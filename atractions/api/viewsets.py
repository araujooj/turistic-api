
from rest_framework.viewsets import ModelViewSet
from atractions.models import Atraction
from .serializers import AttractionsSerializer

class AttractionsViewSet(ModelViewSet):
    queryset = Atraction.objects.all()
    serializer_class = AttractionsSerializer