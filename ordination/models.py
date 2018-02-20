from django.db import models

class Ordination(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
