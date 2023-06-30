from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import Facture
from suppliers.forms import FactureForm
from suppliers.models import Paiement
from suppliers.forms import PaiementForm
from django.contrib.auth.decorators import  login_required

#@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    factures = Facture.objects.all()
    return render(
        request,
        'app/factures/index.html',
        {
            'factures': factures
        }
    )
#@login_required(login_url='/login')

def create(request):
    form = FactureForm()
    return render(
        request, 
        'app/factures/create.html',
        {
            'form': form
        }
    )
#@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        nom = request.POST['commande']
        #facture = request.POST['facture']

        if Facture.objects.filter(commande_id=nom).exists():
            messages.error(request, 'Une Facture avec le même nom de commande existe déjà.')
            return redirect('/paiements')

        #if facture and Paiement.objects.filter(facture_id=facture).exists():
            #messages.error(request, 'Un paiement avec le même numéro de facture existe déjà.')
            #return redirect('/paiements')

        numero_facture = request.POST['numero_facture']
        if Facture.objects.filter(numero_facture=numero_facture).exists():
            messages.error(request, 'Une facture avec ce numéro existe déjà.')
            return redirect('/factures')

        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Invoice has been saved successfully !")
        return redirect('/factures')

#@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = FactureForm()
        else:
            facture = Facture.objects.get(pk=id)
            form = FactureForm(instance=facture)
        return render(
            request,
            'app/factures/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = FactureForm(request.POST)
        else:
            facture = Facture.objects.get(pk=id)
            form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
        messages.success(request, "Invoice has been updated successfully !")
        return redirect('/factures')

#@login_required(login_url='/login')

def delete(request, id):
    facture = Facture.objects.get(pk=id)
    facture.delete()
    messages.success(request, "Invoice has been removed successfully !")
    return redirect('/factures')