from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator



def index(request):
    return render(request,'index.html')

def sessio_user(request):
    # if not request.user.is_authenticated:
    #     return redirect("login")
    return render(request,'session/user.html')

def sessio_consultant(request):
    # if not request.user.is_authenticated:
    #     return redirect("login")
    return render(request,'session/consultant.html')

def liste_user(request):
    # if not request.user.is_authenticated:
    #     return redirect("login")
    liste_obj = User.objects.all()
    paginator = Paginator(liste_obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"liste_user": page_obj}
    return render(request,'liste_users.html',context)

def login(request):
    if request.method=="POST":
        form = Form_connexion(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                if user.status==True:
                    if user.profil_user=="ADMIN":
                        return redirect('home') 
                    if user.profil_user == "CONSULTANT":
                        return redirect('sessio-consultant')
                    if user.profil_user == "UTILISATEUR":
                        return redirect('session-user')
                else:
                   messages.error(request,"Votre compte a été bloquer veuillez contacter l'admin")
                return render(request,'login.html',{'form':form})  
            else:
                messages.error(request,"nom d'utilisateur ou mot de passe incorrecte")
                return render(request,'login.html',{'form':form})
        else:
            messages.error(request,"Tous les champs doivent etre rempli")
            return render(request,'login.html',{'form':form})
    else:
        form = Form_connexion(request.POST)
        return render(request,'login.html',{'form':form})

def Compte(request):
    if request.method == "POST":
        utilisateurs = request.POST['type_user']
        form = Compte_user(request.POST)
        if form.is_valid():
            utilisateur = form.cleaned_data['type_user']
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = User.objects.create(username=username,type_user=utilisateur,password=pwd,status="1")
            user.set_password(pwd)
            user.save()
            
            if utilisateurs == 'ADMIN':
                user.profil_user = "ADMIN"
                user.save()
            if utilisateurs == 'UTILISATEUR':
                user.profil_user = "UTILISATEUR"
                user.save()
            if  utilisateurs == 'CONSULTANT':
                user.profil_user = "CONSULTANT"
                user.save()
  
            if user is not None:
                return redirect('login')
        else:
            messages.error(request,"tous les champs sont obligatoires")
            form = Compte_user()
            contexte = {'form':form}
            return render(request,'register.html',contexte)
    else:
        form = Compte_user()
        contexte = {'form':form}
        return render(request,'register.html',contexte)

def desactiver_user(request,id):
    user = User.objects.get(id=id)
    user.status = False
    user.save()
    return redirect('liste-user')

def activer_user(request,id):
    user = User.objects.get(id=id)
    user.status = True
    user.save()
    return redirect('liste-user')