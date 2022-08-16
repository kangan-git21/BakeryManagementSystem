from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from AdminApp.models import Item
from AdminApp.serializers import ItemSerializer
from CustomerApp.models import Order
from CustomerApp.serializers import OrderSerializer

""" Shopping Cart for what customer orders and view it later"""


class ShoppingCart(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Items': 'Ordered'}, status=status.HTTP_201_CREATED)
        return Response({'Note': "Can't proceed"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        item = Order.objects.all()
        serializer = OrderSerializer(item, many=True)
        return Response(serializer.data)

""" Working on Patch, not completed"""
    # def patch(self, request):
    #     previous_list = Order.objects.get(data=request.data['item'])
    #     return HttpResponse(previous_list)
    #     return HttpResponse(previous_list.id)
    #     if previous_list is not None:
    #         Item.quantity -= request.data['quantity']
    #         return HttpResponse(Item.quantity)
    #









# Create your views here.
