from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import Paiement
from suppliers.forms import PaiementForm
from django.contrib.auth.decorators import  login_required

#@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    paiements = Paiement.objects.all()
    return render(
        request,
        'app/paiements/index.html',
        {
            'paiements': paiements
        }
    )
#@login_required(login_url='/login')

def create(request):
    form = PaiementForm()
    return render(
        request, 
        'app/paiements/create.html',
        {
            'form': form
        }
    )
#@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        form = PaiementForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Paiement has been saved successfully !")
        return redirect('/paiements')

#@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = PaiementForm()
        else:
            paiement = Paiement.objects.get(pk=id)
            form = PaiementForm(instance=paiement)
        return render(
            request,
            'app/paiements/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = PaiementForm(request.POST)
        else:
            paiement = Paiement.objects.get(pk=id)
            form = PaiementForm(request.POST, instance=paiement)
        if form.is_valid():
            form.save()
        messages.success(request, "Paiement has been updated successfully !")
        return redirect('/paiements')

#@login_required(login_url='/login')

def delete(request, id):
    paiement = Paiement.objects.get(pk=id)
    paiement.delete()
    messages.success(request, "Paiement has been removed successfully !")
    return redirect('/paiements')