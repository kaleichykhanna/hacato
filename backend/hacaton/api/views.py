from django.shortcuts import redirect
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cal.models import Event
from .serializers import EventSerializer
from datetime import datetime

@api_view(['GET'])
def index(request):
    current_month = datetime.now().month
    return redirect('monthView', month=current_month)


@api_view(['GET'])
def monthView(request, month):
    current_month = datetime.now().month
    events = Event.objects.filter(Q(date__month__gte=current_month) & Q(date__month=month))
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def mapView(request):
    today = datetime.now().date()
    events = Event.objects.filter(date__gte=today)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


