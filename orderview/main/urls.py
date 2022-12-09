from django.urls import path
from .views import PostSearch

urlpatterns = [
    path('postsearch', PostSearch.as_view(), name="postsearch"  ),
]