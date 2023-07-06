from django.shortcuts import redirect,render
from django.http import HttpRequest
from suppliers.models import Droit
from suppliers.forms import DroitForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url= "/login")
def index(request):
    assert isinstance(request, HttpRequest)
    droits = Droit.objects.all()
    return render(
        request,
        'app/droits/index.html',
        {
            'droits': droits
        }
    )

@login_required(login_url= "/login")   
def create(request):
    form = DroitForm()
    return render(
        request,
        'app/droits/create.html',
        {
            'form' : form
        }
    )
    
@login_required(login_url= "/login")   
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        nom = request.POST['nom']
        if Droit.objects.filter(nom=nom).exists():
            messages.error(request, 'Un Droit avec ce nom existe déjà.')
            return redirect('/droits')

        form = DroitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enregistrer Avec Succes !")
    #retour a la page
    return redirect('/droits')


@login_required(login_url= "/login")
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = DroitForm()
        else:
            droit = Droit.objects.get(pk=id)
            form = DroitForm(instance=droit)
        return render(
            request,
            'app/droits/edit.html',
            {
                'form': form
            }
        )
        
        
# Update a Droit
@login_required(login_url= "/login")
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = DroitForm(request.POST)
        else:
            droit = Droit.objects.get(pk=id)
            form = DroitForm(request.POST, instance=droit)
        if form.is_valid():
            form.save()
        messages.success(request, "Le Droit a été Modifié avec Succes !")
        return redirect('/droits')
    

# Remove a Droit
@login_required(login_url= "/login")    
def delete(request, id):
    assert isinstance(request, HttpRequest)
    droit = Droit.objects.get(pk=id)
    droit.delete()
    messages.success(request, "Le Droit a été Supprimé avec Succes !")
    return redirect('/droits')