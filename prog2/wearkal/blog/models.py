from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class ModeTopic(models.TextChoices):    
        TENDANCE = "Tendance"    
        CULTUREL = "Culturel"    
        HAUTECOUTURE = "Hautecouture"
class SpecTopic(models.TextChoices):    
        COUTUREHOMME = "CoutureHomme"    
        COUTUREFEMME = "CoutureFemme"    
        COUTUREMIXTE = "CoutureMixte"


class patron(models.Model):
        title = models.CharField(unique=True, max_length=100)
        nomode = models.CharField(max_length=30)
        topic = models.CharField(max_length=50, choices=ModeTopic.choices)
        image = models.ImageField(upload_to="blog_images", null=True, blank=True)
        explain = models.TextField(blank=True) 
        is_published = models.BooleanField(default=False) 
        pub_date = models.DateField(null=True, blank=True) 
        def __str__(self):        
                return self.title + ("*" if self.is_published else "")

        def get_absolute_url(self):        
                return "/blog/post/" + str(self.id) + "/"


class MaisonCouture(models.Model):
        nom = models.CharField(max_length=100)
        adresse = models.CharField(max_length=200)
        photo_atel = models.ImageField(upload_to="blog_images", null=True, blank=True)
        telephone = models.CharField(max_length=15)
        specialisation = models.CharField(max_length=50, choices=SpecTopic.choices)
        email = models.EmailField()
        site_web = models.URLField()
        description = models.TextField()
        date_creation = models.DateField()

        def __str__(self):        
                return self.nom
        def get_absolute_url(self):
                return reverse('blog:maison-detail', kwargs={'maison_id': self.id})



class couturier(models.Model):
    nom_complet = models.CharField(max_length=30)   
    nom_populaire = models.CharField(max_length=30)
    contact = models.IntegerField(default=0)
    email = models.CharField(max_length=30)
    #topic = models.CharField(max_length=50, choices=SpecTopic.choices)
    nom_atelier = models.CharField(max_length=30)
    adresse_atelier = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="blog_images", null=True, blank=True)
    

    def __str__(self):        
        return self.nom_complet
    @property
    def recherche_nom_complet(self):
        return self.nom_complet

