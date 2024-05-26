from django.contrib import admin
from django.urls import path
from pages import views as page_views 

app_name  = 'pages'

urlpatterns = [
    path('', page_views.home),
    path('apropos/', page_views.view_name, name='apropos'),
    path('boutique/', page_views.view_nam, name='boutique'),
    path('contact/', page_views.view_na, name='contact'),
    path('voirmodel/', page_views.view_n, name='voirmodel'),
    

  ]   