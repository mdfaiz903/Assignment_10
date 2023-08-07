from django.contrib import admin
from . models import food_model
# Register your models here.
class foodAdmin(admin.ModelAdmin):
    list_display = ('name','color')
admin.site.register(food_model)