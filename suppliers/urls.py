from django.contrib import admin
from django.urls import path
from suppliers.views import categories_produits, fournisseurs, home, produits

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
    path('produits/delete/<int:id>', produits.delete, name='produit'),
        
]