from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import Produit
from suppliers.forms import ProduitForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    produits = Produit.objects.all()
    return render(
        request,
        'app/produits/index.html',
        {
            'produits': produits
        }
    )
@login_required(login_url='/login')

def create(request):
    form = ProduitForm()
    return render(
        request, 
        'app/produits/create.html',
        {
            'form': form
        }
    )
@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Produit has been saved successfully !")
        return redirect('/produits')

@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProduitForm()
        else:
            produit = Produit.objects.get(pk=id)
            form = ProduitForm(instance=produit)
        return render(
            request,
            'app/produits/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = ProduitForm(request.POST)
        else:
            produit = Produit.objects.get(pk=id)
            form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
        messages.success(request, "Produit has been updated successfully !")
        return redirect('/produits')

@login_required(login_url='/login')

def delete(request, id):
    produit = Produit.objects.get(pk=id)
    produit.delete()
    messages.success(request, "Produit has been removed successfully !")
    return redirect('/produits')