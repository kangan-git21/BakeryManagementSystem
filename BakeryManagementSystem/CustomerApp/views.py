from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from AdminApp.models import Item
from AdminApp.serializers import ItemSerializer
from CustomerApp.models import Cart
from CustomerApp.serializers import CartSerializer


class ShoppingCart(APIView):
    def get(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Items': 'Ordered'}, status=status.HTTP_201_CREATED)
        return Response({'Not': 'Received'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        previous_item = Item.objects.get(item_name=request.data['item_name'])
        if previous_item is not None:
            if request.data['quantity'] <= previous_item.quantity:
                previous_item.quantity -= request.data['quantity']
                previous_item.save()
                return Response(previous_item)
            return Response({'Order': 'Received'}, status=status.HTTP_200_OK)
        return Response({'Order': 'Can not be carried out'}, status=status.HTTP_400_BAD_REQUEST)









# Create your views here.
