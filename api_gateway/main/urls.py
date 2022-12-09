from django.urls import path, include

from .views import AddOrders

urlpatterns = [
    path("postorder",AddOrders.as_view(), name="postorder"),
]

