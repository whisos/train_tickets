from django.urls import path
from train_tickets.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('detail/<int:place_id>', place_detail, name = "place_detail"),
]
