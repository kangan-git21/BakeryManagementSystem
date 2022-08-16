from django.db import models


""" The Ingredient Model having list of ingredients present in Stock with name, 
its quantity and cost_price of one ingredient. """


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)  #Price of One ingredient

    def __str__(self):
        return f"{self.name}"


""" Login to the App"""


class LoginUser(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=120)


"""Item present in Bakery having name and quantity"""


class Item(models.Model):
    item_name = models.CharField(max_length=50, unique= True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item_name}"


"""Requirements for a bakery item"""


class Requirements(models.Model):
    need_item = models.ForeignKey(Item, blank=True, default=None, on_delete=models.CASCADE)
    need_ingredients = models.ForeignKey(Ingredient, blank=True, on_delete=models.CASCADE)
    need_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.need_item} of {self.need_ingredients} in {self.need_quantity} quantity"

