from django.shortcuts import render
from . models import food_model
# Create your views here.
def food_view(request):
    obj = food_model.objects.all()
    return render(request,'base.html',{'object':obj})