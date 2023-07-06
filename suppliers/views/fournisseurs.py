from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import Fournisseur
from suppliers.forms import FournisseurForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    fournisseurs = Fournisseur.objects.all()
    return render(
        request,
        'app/fournisseurs/index.html',
        {
            'fournisseurs': fournisseurs
        }
    )
@login_required(login_url='/login')

def create(request):
    form = FournisseurForm()
    return render(
        request, 
        'app/fournisseurs/create.html',
        {
            'form': form
        }
    )
@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        nom_entreprise = request.POST['nom_entreprise']
        if Fournisseur.objects.filter(nom_entreprise=nom_entreprise).exists():
            messages.error(request, 'Un Fournisseur avec ce nom existe déjà.')
            return redirect('/fournisseurs')

        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Fournisseur has been saved successfully !")
        return redirect('/fournisseurs')

@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = FournisseurForm()
        else:
            fournisseur = Fournisseur.objects.get(pk=id)
            form = FournisseurForm(instance=fournisseur)
        return render(
            request,
            'app/fournisseurs/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = FournisseurForm(request.POST)
        else:
            fournisseur = Fournisseur.objects.get(pk=id)
            form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
        messages.success(request, "Fournisseur has been updated successfully !")
        return redirect('/fournisseurs')

@login_required(login_url='/login')

def delete(request, id):
    fournisseur = Fournisseur.objects.get(pk=id)
    fournisseur.delete()
    messages.success(request, "Fournisseur has been removed successfully !")
    return redirect('/fournisseurs')