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
