from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Count, Sum
from suppliers.models import Fournisseur
from suppliers.models import CategorieProduit
from suppliers.models import Commande
from suppliers.models import Paiement
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')

def index(request):
    nbre_fournisseur = Fournisseur.objects.all().count()
    nbre_categorie = CategorieProduit.objects.all().count()
    nbre_commande = Commande.objects.all().count()
    chiffre_affaire = getPaiementPerMonth()
    return render(
        request,
        'app/home/index.html',
        {
            'nbre_fournisseur' : nbre_fournisseur,
            'nbre_categorie' : nbre_categorie,
            'nbre_commande' : nbre_commande,
            'chiffre_affaire': chiffre_affaire
        }
    )
def getPaiementPerMonth():
    total_amount_per_day = Paiement.objects.values('date_paiement','montant',).annotate(total_amount=Sum('montant')).order_by('date_paiement')

    return total_amount_per_day