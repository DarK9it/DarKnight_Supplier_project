from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import CategorieProduit
from suppliers.forms import CategorieProduitForm
from django.contrib.auth.decorators import  login_required

#@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    categories_produits = CategorieProduit.objects.all()
    return render(
        request,
        'app/categories_produits/index.html',
        {
            'categories_produits': categories_produits
        }
    )
#@login_required(login_url='/login')

def create(request):
    form = CategorieProduitForm()
    return render(
        request, 
        'app/categories_produits/create.html',
        {
            'form': form
        }
    )
#@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        nom_categorie = request.POST['nom_categorie']
        if CategorieProduit.objects.filter(nom_categorie=nom_categorie).exists():
            messages.error(request, 'Une catégorie avec ce nom existe déjà.')
            return redirect('/categories_produits')

        form = CategorieProduitForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "CategorieProduit has been saved successfully !")
        return redirect('/categories_produits')

#@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategorieProduitForm()
        else:
            categorie_produit = CategorieProduit.objects.get(pk=id)
            form = CategorieProduitForm(instance=categorie_produit)
        return render(
            request,
            'app/categories_produits/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CategorieProduitForm(request.POST)
        else:
            categorie_produit = CategorieProduit.objects.get(pk=id)
            form = CategorieProduitForm(request.POST, instance=categorie_produit)
        if form.is_valid():
            form.save()
        messages.success(request, "CategorieProduit has been updated successfully !")
        return redirect('/categories_produits')

#@login_required(login_url='/login')

def delete(request, id):
    categorie_produit = CategorieProduit.objects.get(pk=id)
    categorie_produit.delete()
    messages.success(request, "CategorieProduit has been removed successfully !")
    return redirect('/categories_produits')