"""
URL configuration for wearkal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
 

from django.conf import settings             # N E W 
from django.conf.urls.static import static   # N E W

urlpatterns = [

    path('blog/', include('blog.urls')),
    path('',include('pages.urls')),
    
   
         # U r l s f o r a c c o u n t m a n a g e m e n t    
    path('accounts/', include('accounts.urls')), # N E W    
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('admin/', admin.site.urls),
    
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# N E W


