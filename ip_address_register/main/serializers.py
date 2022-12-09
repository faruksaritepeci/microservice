from rest_framework import serializers

from .models import ServerAddress

class ServerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerAddress
        fields = "__all__"
        
