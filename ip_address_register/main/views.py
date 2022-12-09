# Global Imports
## Django libs
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core import serializers

## Rest Framework libs
from rest_framework.views import APIView
from rest_framework.response import Response

# Local Imports
from .models import ServerAddress
from .serializers import ServerAddressSerializer


class AddressAPIView(APIView):
    
    def get(self, request):
        addresses = ServerAddress.objects.all()
        serializer = ServerAddressSerializer(addresses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ServerAddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
            