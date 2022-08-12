from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)  #Price of One ingredient

    def __str__(self):
        return f"{self.name}"


class LoginUser(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=120)


class Item(models.Model):
    item_name = models.CharField(max_length=50, )   #Removed unique=True
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item_name}"


class Requirements(models.Model):
    need_item = models.ForeignKey(Item, blank=True, default=None, on_delete=models.CASCADE)
    need_ingredients = models.ForeignKey(Ingredient, blank=True, on_delete=models.CASCADE)
    need_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.need_item} of {self.need_ingredients} in {self.need_quantity} quantity"

