from django.db import models

class Person(models.Model):  
        first_name = models.CharField(max_length=30)   
        last_name = models.CharField(max_length=30)

class BlogPost(models.Model):    
        title = models.CharField(unique=True, max_length=100)    
        content = models.TextField(blank=True)    
        num_views = models.IntegerField(default=0)    
        is_published = models.BooleanField(default=False)    
        pub_date = models.DateField(null=True, blank=True)
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

        def __str__(self):        
                return self.title

                                         

# Create your models here.
