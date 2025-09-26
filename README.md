# Ex02 Django ORM Web Application
## Date: 26-09-2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

<img width="1172" height="626" alt="Screenshot 2025-09-26 121047" src="https://github.com/user-attachments/assets/613497f9-5dca-46e9-a938-169266c108cc" />


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
admin.py


from django.contrib import admin
from . models import car
# Register your models here.

admin.site.register(car)

class arAdmin(admin.ModelAdmin):
    list_display = ('id','brand','model','year','price')

models.py


from django.db import models

# Create your models here.
class car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=30)
    year = models.DateField()
    price = models.IntegerField()
```

## OUTPUT

![alt text](<Screenshot 2025-09-26 121034.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
