from django.contrib import admin

# Register your models here.
from AdminApp.views import Ingredient, Item, Requirements

admin.site.register(Ingredient)
admin.site.register(Item)
admin.site.register(Requirements)
