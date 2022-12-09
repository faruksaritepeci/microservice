# Global Imports
import requests

## Django libs
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.db.models import Q

## Rest Framework libs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Local Imports
from .serializers import OrderSerializer, OrderFilterModelSerializer
from .models import Order

# Static urlbook for now, will convert to dynamic via, ip_address_register
urlbook = [
    {"serverType": "ip_address_register", "serverURL": "127.0.0.1:8000"},
    {"serverType": "orderview", "serverURL": "127.0.0.4:8000"},
    {"serverType": "ordercontroller", "serverURL": "127.0.0.5:8000"},
]
    

### REAL API INTERFACE FOR OTHER SERVICES

class PostOrder(APIView):
    
    def post(self, request):
        print(request.data)
        serializer = OrderSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for order in serializer.data:
            order = OrderSerializer(data=order, many=False)
            order.is_valid(raise_exception=True)
            if order.validated_data["BrandId"] != 0:
                order.save()
        return Response(status=200)
        
class PostOrderFilter(APIView):
    
    def post(self, request):
        print(request.data)
        serializer = OrderFilterModelSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        
        searchFilter = serializer.validated_data
        
        startIndex = searchFilter["PageSize"] * (searchFilter["PageNumber"] - 1)
        endIndex = startIndex + searchFilter["PageSize"]
        
        page = Order.objects.filter(CustomerName__contains = searchFilter["SearchText"]
                            ).filter(CreatedOn__gt = searchFilter["StartDate"]
                            ).filter(CreatedOn__lt = searchFilter["EndDate"]
                            ).filter(Q(Status = 10) | Q(Status = 20)
                            ).order_by(searchFilter["SortBy"]
                                
                            )[startIndex: endIndex]   
                            
        
        orderSerializer = OrderSerializer(data=page, many=True)
        orderSerializer.is_valid(raise_exception=False)
        
        responsetext = "["
        for item in orderSerializer.validated_data:
            responsetext += str(item) + ",\n"
        
        responsetext += "]"
        
        #return Response(orderSerializer.data)
        return Response(responsetext)