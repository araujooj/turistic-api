from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import TuristicPoint
from .serializer import TuristicPointSerializer


class TuristicPointViewSet(ModelViewSet):
    serializer_class = TuristicPointSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')

        queryset = TuristicPoint.objects.filter(approved=True)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @action(methods=['GET'], detail=True)
    def denounce(self, request, pk=None):
        return Response({'hello': 'Denunciado'})
