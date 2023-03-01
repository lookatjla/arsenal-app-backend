from django.shortcuts import render
from .models import Exercise
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ExerciseSerializer
# Create your views here.

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.AllowAny]