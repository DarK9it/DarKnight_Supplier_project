from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Count, Sum, Avg
from datetime import date
from suppliers.models import Fournisseur
from suppliers.models import CategorieProduit
from suppliers.models import Commande, DetailCommande
from suppliers.models import Paiement, NoteFournisseur, Stock
from django.contrib.auth.decorators import  login_required
import datetime

@login_required(login_url='/login')

def index(request):
    nbre_fournisseur = Fournisseur.objects.all().count()
    nbre_categorie = CategorieProduit.objects.all().count()
    nbre_commande = Commande.objects.all().count()
    chiffre_affaire = getPaiementPerMonth()
    categories = count_categorie()
    status = count_status()
    debut_periode = datetime.datetime(2023, 1, 1)
    fin_periode = datetime.datetime(2030, 1, 31)
    note_moyenne = NoteFournisseur.objects.aggregate(moyenne=Avg('note'))['moyenne']
    return render(
        request,
        'app/home/index.html',
        {
            'nbre_fournisseur' : nbre_fournisseur,
            'nbre_categorie' : nbre_categorie,
            'nbre_commande' : nbre_commande,
            'chiffre_affaire': chiffre_affaire,
            'categories': categories,
            'status': status,
            'note_moyenne': note_moyenne
        }
    )

def getPaiementPerMonth():
    total_amount_per_day = Paiement.objects.values('date_paiement','montant').annotate(total_amount=Sum('montant')).order_by('date_paiement')

    return total_amount_per_day

def count_categorie():
    categories = {}
    for detail in DetailCommande.objects.all():
        if detail.categorie not in categories:
            categories[detail.categorie] = 0
        categories[detail.categorie] += 1
    return categories

def count_status():
    commandes = Commande.objects.all()
    statut_counts = {}
    for commande in commandes:
        statut = commande.statut
        if statut not in statut_counts:
            statut_counts[statut] = 0
        statut_counts[statut] += 1
    return statut_counts