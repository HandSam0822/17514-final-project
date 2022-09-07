from django.urls import path, include
from mycmu import views

urlpatterns = [
     path("", include("mycmu.urls")),
]
