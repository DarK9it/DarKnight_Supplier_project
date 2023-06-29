from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import HistoriqueCommande
from suppliers.forms import HistoriqueCommandeForm
from django.contrib.auth.decorators import  login_required

#@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    historiques_commandes = HistoriqueCommande.objects.all()
    return render(
        request,
        'app/historiques_commandes/index.html',
        {
            'historiques_commandes': historiques_commandes
        }
    )
#@login_required(login_url='/login')

def create(request):
    form = HistoriqueCommandeForm()
    return render(
        request, 
        'app/historiques_commandes/create.html',
        {
            'form': form
        }
    )
#@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        form = HistoriqueCommandeForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "HistoriqueCommande has been saved successfully !")
        return redirect('/historiques_commandes')

#@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = HistoriqueCommandeForm()
        else:
            historique_commande = HistoriqueCommande.objects.get(pk=id)
            form = HistoriqueCommandeForm(instance=historique_commande)
        return render(
            request,
            'app/historiques_commandes/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = HistoriqueCommandeForm(request.POST)
        else:
            historique_commande = HistoriqueCommande.objects.get(pk=id)
            form = HistoriqueCommandeForm(request.POST, instance=historique_commande)
        if form.is_valid():
            form.save()
        messages.success(request, "HistoriqueCommande has been updated successfully !")
        return redirect('/historiques_commandes')

#@login_required(login_url='/login')

def delete(request, id):
    historique_commande = HistoriqueCommande.objects.get(pk=id)
    historique_commande.delete()
    messages.success(request, "HistoriqueCommande has been removed successfully !")
    return redirect('/historiques_commandes')