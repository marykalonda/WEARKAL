from django.contrib import admin


# import the models 
from .models import *


# register each model with the admin site
admin.site.register(BlogPost)
admin.site.register(couturier)


# Register your models here.
