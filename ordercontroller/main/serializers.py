from rest_framework import serializers

from .models import Order, OrderFilterModel

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        
class OrderFilterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderFilterModel
        fields = "__all__"
