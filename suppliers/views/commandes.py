from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import Commande
from suppliers.forms import CommandeForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    commandes = Commande.objects.all()
    return render(
        request,
        'app/commandes/index.html',
        {
            'commandes': commandes
        }
    )
@login_required(login_url='/login')

def create(request):
    form = CommandeForm()
    return render(
        request, 
        'app/commandes/create.html',
        {
            'form': form
        }
    )
@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        if Commande.objects.filter(nom=nom).exists():
            messages.error(request, 'Une Commande avec ce nom existe déjà.')
            return redirect('/commandes')

        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Commande has been saved successfully !")
        return redirect('/commandes')

@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CommandeForm()
        else:
            commande = Commande.objects.get(pk=id)
            form = CommandeForm(instance=commande)
        return render(
            request,
            'app/commandes/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CommandeForm(request.POST)
        else:
            commande = Commande.objects.get(pk=id)
            form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
        messages.success(request, "Commande has been updated successfully !")
        return redirect('/commandes')

@login_required(login_url='/login')

def delete(request, id):
    commande = Commande.objects.get(pk=id)
    commande.delete()
    messages.success(request, "Commande has been removed successfully !")
    return redirect('/commandes')