from django.contrib import admin


# import the models 
from .models import *


# register each model with the admin site
admin.site.register(patron)
admin.site.register(couturier)
admin.site.register(MaisonCouture)


# Register your models here.
