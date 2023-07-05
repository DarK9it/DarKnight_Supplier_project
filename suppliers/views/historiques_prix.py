from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import HistoriquePrix
from suppliers.forms import HistoriquePrixForm
from django.contrib.auth.decorators import  login_required

#@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    historiques_prix = HistoriquePrix.objects.all()
    return render(
        request,
        'app/historiques_prix/index.html',
        {
            'historiques_prix': historiques_prix
        }
    )
#@login_required(login_url='/login')

def create(request):
    form = HistoriquePrixForm()
    return render(
        request, 
        'app/historiques_prix/create.html',
        {
            'form': form
        }
    )
#@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        form = HistoriquePrixForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Price History has been saved successfully !")
        return redirect('/historiques_prix')

#@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = HistoriquePrixForm()
        else:
            historique_prix = HistoriquePrix.objects.get(pk=id)
            form = HistoriquePrixForm(instance=historique_prix)
        return render(
            request,
            'app/historiques_prix/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = HistoriquePrixForm(request.POST)
        else:
            historique_prix = HistoriquePrix.objects.get(pk=id)
            form = HistoriquePrixForm(request.POST, instance=historique_prix)
        if form.is_valid():
            form.save()
        messages.success(request, "Price History has been updated successfully !")
        return redirect('/historiques_prix')

#@login_required(login_url='/login')

def delete(request, id):
    historique_prix = HistoriquePrix.objects.get(pk=id)
    historique_prix.delete()
    messages.success(request, "Price History has been removed successfully !")
    return redirect('/historiques_prix')