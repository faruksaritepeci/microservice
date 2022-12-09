# Global Imports
import requests

## Django libs
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core import serializers

## Rest Framework libs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Local Imports

# Static urlbook for now, will convert to dynamic via, ip_address_register
urlbook = [
    {"serverType": "ip_address_register", "serverURL": "127.0.0.1:8000"},
    {"serverType": "orderview", "serverURL": "127.0.0.4:8000"},
    {"serverType": "ordercontroller", "serverURL": "127.0.0.5:8000"},
]
    

### REAL API INTERFACE FOR CLIENT

class AddOrders(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def post(self, request):
        
        ordercontrollerIP = None
        for server in urlbook:
            if server["serverType"] == "ordercontroller":
                ordercontrollerIP = server["serverURL"]
        if ordercontrollerIP == None:
            return Response(status=404)        
        APIresponse = requests.post("http://" + ordercontrollerIP + "/api/postorder", request.body, headers={'content-type': 'application/json'})
        
        return Response(APIresponse.status_code)
    
    
class SearchOrders(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def post(self, request):
        return Response(request.user.id)
        orderviewIP = None
        for server in urlbook:
            if server["serverType"] == "orderview":
                orderviewIP = server["serverURL"]
        if orderviewIP == None:
            return Response(status=404)
                
        APIresponse = requests.post("http://" + orderviewIP + "", request.POST).json()
        
        return Response(APIresponse)
    
