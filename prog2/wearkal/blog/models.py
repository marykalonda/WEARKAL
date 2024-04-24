from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission



User = settings.AUTH_USER_MODEL



# class Person(models.Model):  
#         first_name = models.CharField(max_length=30)   
#         last_name = models.CharField(max_length=30)

class BlogPost(models.Model): 
        class Meta:        
                permissions = [            
                        ("publish_blogpost", "Can publish a BlogPost")        
                ]
        author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
        title = models.CharField(unique=True, max_length=100)    
        content = models.TextField(blank=True)    
        num_views = models.IntegerField(default=0)    
        is_published = models.BooleanField(default=False)    
        pub_date = models.DateField(null=True, blank=True)
        def __str__(self):        
                return self.title + ("*" if self.is_published else "")

        def get_absolute_url(self):        
                return "/blog/post/" + str(self.id) + "/"
class patron(models.Model):
        nomode = models.CharField(max_length=30)
        explain = models.TextField(blank=True) 
        pub_date = models.DateField(null=True, blank=True)   

class atelier(models.Model):
        name = models.CharField(max_length=30)
        adresse = models.CharField(max_length=30)
        contact = models.IntegerField(default=0)

class couturier(models.Model):
        first_name = models.CharField(max_length=30)   
        last_name = models.CharField(max_length=30)
        numero = models.IntegerField(default=0)
        adresseatel = models.CharField(max_length=30)


    




        
                                         

# Create your models here.
