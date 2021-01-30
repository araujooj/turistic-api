from rest_framework.viewsets import ModelViewSet
from core.models import TuristicPoint
from .serializer import TuristicPointSerializer

class TuristicPointViewSet(ModelViewSet):

    queryset = TuristicPoint.objects.all()
    serializer_class = TuristicPointSerializer
