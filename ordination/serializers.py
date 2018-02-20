from rest_framework import serializers
from ordination import models

class OrdinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ordination
        fields = '__all__'

