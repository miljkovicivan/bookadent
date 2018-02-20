from django.db import models

class Ordination(models.Model):
    name = models.stringField(max_length=100)
