from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Grocery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('groceries-index', kwargs={'grocery_id': self.id})
    
    class Meta:
        ordering = ['id']