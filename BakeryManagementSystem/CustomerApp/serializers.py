from rest_framework import serializers

from CustomerApp.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['item', 'quantity', 'status']

