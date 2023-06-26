from django.contrib import admin
from django.urls import path
from suppliers.views import categories_produits,commandes, details_commandes,fournisseurs, home, produits,paiements, historiques_prix

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('fournisseurs/', fournisseurs.index, name='fournisseurs_index'),
    path('fournisseurs/create', fournisseurs.create, name='fournisseurs_create'),
    path('fournisseurs/store', fournisseurs.store, name='fournisseurs_store'),
    path('fournisseurs/edit/<int:id>', fournisseurs.edit, name='fournisseurs_edit'),
    path('fournisseurs/delete/<int:id>', fournisseurs.delete, name='fournisseurs_delete'),

    path('categories_produits/', categories_produits.index, name='categories_produits_index'),
    path('categories_produits/create', categories_produits.create, name='categories_produits_create'),
    path('categories_produits/store', categories_produits.store, name='categories_produits_store'),
    path('categories_produits/edit/<int:id>', categories_produits.edit, name='categories_produits_edit'),
    path('categories_produits/delete/<int:id>', categories_produits.delete, name='categories_produits_delete'),

    path('produits/', produits.index, name='produits_index'),
    path('produits/create', produits.create, name='produits_create'),
    path('produits/store', produits.store, name='produits_store'),
    path('produits/edit/<int:id>', produits.edit, name='produits_edit'),
    path('produits/delete/<int:id>', produits.delete, name='produits_delete'),

    path('commandes/', commandes.index, name='commandes_index'),
    path('commandes/create', commandes.create, name='commandes_create'),
    path('commandes/store', commandes.store, name='commandes_store'),
    path('commandes/edit/<int:id>', commandes.edit, name='commandes_edit'),
    path('commandes/delete/<int:id>', commandes.delete, name='commandes_delete'),

    path('details_commandes/', details_commandes.index, name='details_commandes_index'),
    path('details_commandes/create', details_commandes.create, name='details_commandes_create'),
    path('details_commandes/store', details_commandes.store, name='details_commandes_store'),
    path('details_commandes/edit/<int:id>', details_commandes.edit, name='details_commandes_edit'),
    path('details_commandes/delete/<int:id>', details_commandes.delete, name='details_commandes_delete'),

    path('paiements/', paiements.index, name='paiements_index'),
    path('paiements/create', paiements.create, name='paiements_create'),
    path('paiements/store', paiements.store, name='paiements_store'),
    path('paiements/edit/<int:id>', paiements.edit, name='paiements_edit'),
    path('paiements/delete/<int:id>', paiements.delete, name='paiements_delete'), 

    path('historiques_prix/', historiques_prix.index, name='historiques_prix_index'),
    path('historiques_prix/create', historiques_prix.create, name='historiques_prix_create'),
    path('historiques_prix/store', historiques_prix.store, name='historiques_prix_store'),
    path('historiques_prix/edit/<int:id>', historiques_prix.edit, name='historiques_prix_edit'),
    path('historiques_prix/delete/<int:id>', historiques_prix.delete, name='historiques_prix_delete'),
]