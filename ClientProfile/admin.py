from django.contrib import admin

# Register your models here.

#importing ClientProfile class from Model
from .models import ClientProfile  
admin.site.register((ClientProfile))