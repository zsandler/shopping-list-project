from django.db import models
from django.urls import reverse

class Grocery(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('groceries-index', kwargs={'grocery_id': self.id})
    
    class Meta:
        ordering = ['id']