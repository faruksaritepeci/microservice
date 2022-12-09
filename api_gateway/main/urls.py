from django.urls import path, include

from .views import AddOrders, SearchOrders

urlpatterns = [
    path("postorder",AddOrders.as_view(), name="postorder"),
    path("postsearch",SearchOrders.as_view(), name="searchorders"),
]

