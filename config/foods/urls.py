
from django.urls import path
from . views import food_view
urlpatterns = [
  
    path('',food_view,name='food_view'),
]
