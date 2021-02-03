from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.models import TuristicPoint
from .serializer import TuristicPointSerializer


class TuristicPointViewSet(ModelViewSet):
    serializer_class = TuristicPointSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        name = self.request.query_params.get('name')

        queryset = TuristicPoint.objects.filter(approved=True)

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @action(methods=['GET'], detail=True)
    def denounce(self, request, pk=None):
        return Response({'hello': 'Denunciado'})
