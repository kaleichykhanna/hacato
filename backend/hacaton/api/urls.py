from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>', views.monthView, name='monthView'),
    path('map', views.mapView, name='mapView')
]
