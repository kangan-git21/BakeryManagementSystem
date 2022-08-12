from django.db import models
from AdminApp.models import Item, Ingredient


class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item} of {self.quantity}"






# Create your models here.
