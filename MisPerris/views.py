from .models import PerrosRescatados
from rest_framework import viewsets
from MisPerris.serializers import PerrosSerializer

class PerrosViewSet (viewsets.ModelViewSet):
    queryset = PerrosRescatados.objects.all()
    serializer_class = PerrosSerializer