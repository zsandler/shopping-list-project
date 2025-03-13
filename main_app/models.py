from django.db import models

class Grocery(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name