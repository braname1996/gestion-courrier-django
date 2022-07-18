from django.db import models
from django.db.models import fields
from .models import User
from django import forms
from django.forms import ModelForm, widgets



class Form_connexion(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Compte_user(ModelForm):
    class Meta:
        model = User
        fields = ['type_user','username','password']

        labels = {
            'username':"Nom d'utilisateur",
             'password':"Mot de passe"
        }

        help_texts = {
            "username":None
        }

        widgets = {
            'type_user':forms.Select(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
           
        }