from django.shortcuts import render
from .models import Fighter
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import FighterSerializer

# Create your views here.
class FighterViewSet(viewsets.ModelViewSet):
    # the main query for the index route
    queryset = Fighter.objects.all()
    # the serializer class for serializing output
    serializer_class = FighterSerializer
    # optional permission class to set permission level
    permission_classes = [permissions.AllowAny]