from rest_framework import serializers

from CustomerApp.models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['item_list', 'quantity']

