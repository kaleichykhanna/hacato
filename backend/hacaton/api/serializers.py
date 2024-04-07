from rest_framework import serializers 
from cal.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 
                  'date',
                  'time',
                  'university_building',
                  'description',
                  'faculty',
                  'url']