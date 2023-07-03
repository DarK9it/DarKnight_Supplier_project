from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import NoteFournisseur
from suppliers.forms import NoteFournisseurForm
from django.contrib.auth.decorators import  login_required

#@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    notes_fournisseurs = NoteFournisseur.objects.all()
    return render(
        request,
        'app/notes_fournisseurs/index.html',
        {
            'notes_fournisseurs': notes_fournisseurs
        }
    )
#@login_required(login_url='/login')

def create(request):
    form = NoteFournisseurForm()
    return render(
        request, 
        'app/notes_fournisseurs/create.html',
        {
            'form': form
        }
    )
#@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        nom = request.POST['fournisseur']

        if NoteFournisseur.objects.filter(fournisseur_id=nom).exists():
            messages.error(request, 'La note de ce Fournisseur existe déjà.')
            return redirect('/notes_fournisseurs')

        form = NoteFournisseurForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "NoteFournisseur has been saved successfully !")
        return redirect('/notes_fournisseurs')

#@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = NoteFournisseurForm()
        else:
            note_fournisseur = NoteFournisseur.objects.get(pk=id)
            form = NoteFournisseurForm(instance=note_fournisseur)
        return render(
            request,
            'app/notes_fournisseurs/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = NoteFournisseurForm(request.POST)
        else:
            note_fournisseur = NoteFournisseur.objects.get(pk=id)
            form = NoteFournisseurForm(request.POST, instance=note_fournisseur)
        if form.is_valid():
            form.save()
        messages.success(request, "NoteFournisseur has been updated successfully !")
        return redirect('/notes_fournisseurs')

#@login_required(login_url='/login')

def delete(request, id):
    note_fournisseur = NoteFournisseur.objects.get(pk=id)
    note_fournisseur.delete()
    messages.success(request, "NoteFournisseur has been removed successfully !")
    return redirect('/notes_fournisseurs')