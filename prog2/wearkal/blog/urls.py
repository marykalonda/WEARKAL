from django.contrib import admin
from django.urls import path
from . import views


app_name = 'blog' 
urlpatterns = [    
     path('', views.home, name='home'),      
     path('post/<int:post_id>/', views.blog_post_view, name='post_view'),
     path('post/<int:post_id>/', views.blog_post_detail, name='post-detail'),
     path('post/add/', views.blog_post_add, name='post-add'),
     path('post/<int:post_id>/change/', views.blog_post_change, name='post-change'),
     path('post/<int:post_id>/delete/', views.blog_post_delete, name='post-delete'),
     path('post/<int:post_id>/publish/', views.blog_post_publish, name='post-publish'),
     #-----------------------------------------------------------------------------------
     path('couturier/', views.cout_home, name='cout-home'),      
     path('couturier/<int:id>/view', views.cout_view, name='cout-view'),
     path('couturier/search/', views.search_view, name='search'),
     path('couturier/<int:id>/delete', views.cout_delete, name='cout-delete'),
     #-------------------------------------------------------------------------------------
     path('atelier/', views.maisoncouture_list, name='maison-list'),      
     path('atelier/<int:maison_id>/', views.maisoncouture_detail, name='maison-detail'),
     path('atelier/add/', views.maisoncouture_add, name='maison-add'),
     path('atelier/<int:maison_id>/change/', views.maisoncouture_change, name='maison-change'),
     path('atelier/<int:maison_id>/delete/', views.maisoncouture_delete, name='maison-delete'),
     #-------------------------------------------------------------------------------------------
     
    
    ]
