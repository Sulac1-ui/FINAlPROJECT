from django.urls import path
from .views import *


app_name = "ecomapp"
urlpatterns = [
    path("", Homeview.as_view(), name="index")
]
