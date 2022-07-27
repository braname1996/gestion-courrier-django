from django.db import models
#from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import AbstractUser


type = (
    ("ADMIN","ADMIN"),
    ("UTILISATEUR","UTILISATEUR"),
    ("CONSULTANT","CONSULTANT")
)

actifs = (("ACTIF","ACTIF"),("INACTIF","INACTIF"))
class User(AbstractUser):
    type_user = models.CharField(max_length=20, choices=type, default="UTILISATEUR")
    status = models.BooleanField(max_length=25, choices=actifs, default="1", null=True)
    profil_user = models.CharField(max_length=30,default="UTILISATEUR", null=True)

class Courrier(models.Model):
    chargeur = models.CharField(null=True, blank=True, max_length=250)
    destinataire = models.CharField(null=True, blank=True, max_length=250)
    notifier = models.CharField(null=True, blank=True, max_length=250)
    police_de_cargaison = models.CharField(null=True, blank=True, max_length=250)
    date_depart = models.CharField(max_length=250,null=True, blank=True)
    date_arrivee = models.CharField(max_length=250, null=True, blank=True)
    transporteur = models.CharField(null=True, blank=True, max_length=250)
    transitaire = models.CharField(null=True, blank=True, max_length=250)
    operation = models.CharField(null=True, blank=True, max_length=10)
    tarif = models.CharField(null=True, blank=True, max_length=10)
    navire_et_numeroVoyage = models.CharField(null=True, blank=True, max_length=250)
    port_Chargement = models.CharField(null=True, blank=True, max_length=250)
    port_Dechargement = models.CharField(null=True, blank=True, max_length=250)
    estination_finale = models.CharField(null=True, blank=True, max_length=250)
    monaie = models.CharField(null=True, blank=True, max_length=10)
    cout_des_articles = models.FloatField(null=True, blank=True)
    emmision_du_besc = models.FloatField(null=True, blank=True)
    cout_toal = models.FloatField(null=True, blank=True)
    valeur_marchandise = models.FloatField(null=True, blank=True)
    cout_assurance = models.FloatField(null=True, blank=True)
    valeur_Fob = models.FloatField(null=True, blank=True)
    autre_valeur= models.CharField(null=True, blank=True, max_length=30)

    ######################   conteneur  ##################################
    nombre_conteaneur = models.IntegerField(null=True, blank=True)
    Marchandise = models.CharField(null=True, blank=True, max_length=10)
    type_conteneur = models.CharField(null=True, blank=True, max_length=10)
    dimension = models.CharField(null=True, blank=True, max_length=10)
    
    #####################   Notes      ###################################
    note = models.CharField(null=True, blank=True, max_length=10)
    


    def __str__(self):
        return self.destinataire
















