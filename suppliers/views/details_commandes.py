from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import DetailCommande
from suppliers.forms import DetailCommandeForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    details_commandes = DetailCommande.objects.all()
    return render(
        request,
        'app/details_commandes/index.html',
        {
            'details_commandes': details_commandes
        }
    )
@login_required(login_url='/login')

def create(request):
    form = DetailCommandeForm()
    return render(
        request, 
        'app/details_commandes/create.html',
        {
            'form': form
        }
    )
@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        form = DetailCommandeForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Order Detail has been saved successfully !")
        return redirect('/details_commandes')

@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = DetailCommandeForm()
        else:
            detail_commande = DetailCommande.objects.get(pk=id)
            form = DetailCommandeForm(instance=detail_commande)
        return render(
            request,
            'app/details_commandes/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = DetailCommandeForm(request.POST)
        else:
            detail_commande = DetailCommande.objects.get(pk=id)
            form = DetailCommandeForm(request.POST, instance=detail_commande)
        if form.is_valid():
            form.save()
        messages.success(request, "Order Detail has been updated successfully !")
        return redirect('/details_commandes')

@login_required(login_url='/login')

def delete(request, id):
    detail_commande = DetailCommande.objects.get(pk=id)
    detail_commande.delete()
    messages.success(request, "Order Detail has been removed successfully !")
    return redirect('/details_commandes')