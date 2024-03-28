from django.contrib import admin


# import the models 
from .models import BlogPost
from .models import couturier

# register each model with the admin site 
admin.site.register(couturier)


# Register your models here.
