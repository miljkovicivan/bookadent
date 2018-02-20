from django.shortcuts import render
from rest_framework import generics
from ordination import models, serializers


class ListOrdinationView(generics.ListAPIView):
    queryset = models.Ordination.objects.all()
    serializer_class = serializers.OrdinationSerializer
