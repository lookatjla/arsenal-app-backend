from rest_framework import serializers
from .models import Exercise


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Which model will get serialized by this class
        model = Exercise
        # Which fields should be included in the output
        fields = ['exercise_name', 'length_of_workout',
                  'resistance', 'comments']
