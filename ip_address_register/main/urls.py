from django.urls import path

# Local imports
from .views import AddressAPIView

urlpatterns = [
    path("address", AddressAPIView.as_view(), name="geturls"),
    
]
