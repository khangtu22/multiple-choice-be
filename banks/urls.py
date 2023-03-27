from django.urls import path
from .views import ImportAPIView

urlpatterns = [
    path('', ImportAPIView.as_view())
]
