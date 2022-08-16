from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Ingredient, Item, LoginUser

"""User (from django)"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password']


"""Login User"""


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['username', 'password']


"""Ingredients"""


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'cost_price']


"""Item"""


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'quantity']

