from django.urls import path
from rest_framework import routers
from ordination import views

router = routers.DefaultRouter()

app_name = 'ordination'

urlpatterns = [
    path('', views.ListOrdinationView.as_view(), name='ordination')
]

