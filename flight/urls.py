from django.urls import path
from rest_framework import routers
from flight import views

router = routers.DefaultRouter()

app_name = 'flight'

urlpatterns = [
    path('', views.GetFlights.as_view(), name='ordination')
]

