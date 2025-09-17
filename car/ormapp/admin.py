
from django.contrib import admin
from . models import car
# Register your models here.

admin.site.register(car)

class arAdmin(admin.ModelAdmin):
    list_display = ('id','brand','model','year','price')