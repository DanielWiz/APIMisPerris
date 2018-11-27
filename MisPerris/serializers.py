from .models import PerrosRescatados
from rest_framework import serializers

class PerrosSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerrosRescatados
        fields = ('Fotografia','NombrePerro','RazaPredominante','Descripcion','Estado')