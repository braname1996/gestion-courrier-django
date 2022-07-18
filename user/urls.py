from django.urls import path
from .views import *
urlpatterns = [
    path('home/', index, name="home"),
    path('liste/', liste_user, name="liste-user"),
    path('',login, name='login'),
    path('create',Compte, name='create-user'),
    path('liste/<int:id>',desactiver_user, name='bloquer-user'),
    path('listes/<int:id>',activer_user, name='activer-user'),

    path('user/',sessio_user, name='session-user'),
    path('consultant/',sessio_consultant, name='sessio-consultant'),


]