from django.contrib import admin
from django.urls import path
from suppliers.views import fournisseurs

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('fournisseurs/', fournisseurs.index, name='fournisseurs_index'),
    path('fournisseurs/create', fournisseurs.create, name='fournisseurs_create'),
    path('fournisseurs/store', fournisseurs.store, name='fournisseurs_store'),
    path('fournisseurs/edit/<int:id>', fournisseurs.edit, name='fournisseurs_edit'),
    path('fournisseurs/delete/<int:id>', fournisseurs.delete, name='fournisseurs_delete'),
        
]