from .models import Fighter
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our FighterSerializer
class FighterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Fighter
        # the fields that should be included in the serialized output
        fields = ['id', 'firstName', 'lastName', 'nickname', 'currentDivision', 'record', 'img', 'age']