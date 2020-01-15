from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from macropoloapi.models import *


class FoodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Food
        url = serializers.HyperlinkedIdentityField(
            view_name='food',
            lookup_field='id'
        )
        fields = ('id', 'name', 'fat', 'carb', 'protein',
                  'sodium', 'fiber', 'count', 'user_id')
        
class Foods(ViewSet):
    
    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(
            foods,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
