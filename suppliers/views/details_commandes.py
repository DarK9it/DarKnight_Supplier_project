from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from suppliers.models import DetailCommande
from suppliers.models import CategorieProduit, Produit
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
    assert isinstance(request, HttpRequest)
    form = DetailCommandeForm()
    categories = CategorieProduit.objects.all()
    return render(
        request, 
        'app/details_commandes/create.html',
        {
            'form': form,
            'categories':categories
        }
    )
@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        commande = request.POST['commande']
        if DetailCommande.objects.filter(commande=commande).exists():
            messages.error(request, 'Une Commande avec ce nom existe déjà.')
            return redirect('/details_commandes')
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

@login_required(login_url='/login')

def getProducts(request):
    id_categorie= request.GET.get('id_categorie')
    produits = Produit.objects.filter(categorie_id = id_categorie)
    return render(
        request,
        'app/details_commandes/getProducts.html',
        {
            'produits': produits
        }
    )

@login_required(login_url='/login')

def getUnitPrice(request):
    id_produit = request.GET.get('id_produit')
    produit = Produit.objects.get(pk=id_produit)
    return render(
        request,
        'app/details_commandes/getUnitPrice.html',
        {
            'produit': produit
        }
    )

def get_produits_by_categorie(request):
    categorie_id = request.GET.get('categorie_id')
    produits = Produit.objects.filter(categorie_id=categorie_id)
    data = [{'id': p.id, 'nom': p.nom} for p in produits]
    return JsonResponse(data, safe=False)