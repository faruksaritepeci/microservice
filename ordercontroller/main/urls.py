from django.urls import path
from .views import PostOrder, PostOrderFilter

urlpatterns = [
    path('postorder', PostOrder.as_view(), name="postorder"),
    path('postorderfilter', PostOrderFilter.as_view(), name="postorderfilter"),
]