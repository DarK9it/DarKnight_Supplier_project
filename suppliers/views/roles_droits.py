from django.shortcuts import redirect,render
from django.http import HttpRequest
from suppliers.models import RoleDroit
from suppliers.forms import RoleDroitForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#@login_required(login_url= "/login")
def index(request):
    assert isinstance(request, HttpRequest)
    roles_droits = RoleDroit.objects.all()
    return render(
        request,
        'app/roles_droits/index.html',
        {
            'roles_droits': roles_droits
        }
    )

#@login_required(login_url= "/login")   
def create(request):
    form = RoleDroitForm()
    return render(
        request,
        'app/roles_droits/create.html',
        {
            'form' : form
        }
    )
    
#@login_required(login_url= "/login")   
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = RoleDroitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enregistrer Avec Succes !")
    #retour a la page
    return redirect('/roles_droits')


#@login_required(login_url= "/login")
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = RoleDroitForm()
        else:
            role_droit = RoleDroit.objects.get(pk=id)
            form = RoleDroitForm(instance=role_droit)
        return render(
            request,
            'app/roles_droits/edit.html',
            {
                'form': form
            }
        )
        
        
# Update a RoleDroit
#@login_required(login_url= "/login")
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = RoleDroitForm(request.POST)
        else:
            role_droit = RoleDroit.objects.get(pk=id)
            form = RoleDroitForm(request.POST, instance=role_droit)
        if form.is_valid():
            form.save()
        messages.success(request, "Le RoleDroit a été Modifié avec Succes !")
        return redirect('/roles_droits')
    

# Remove a RoleDroit
#@login_required(login_url= "/login")    
def delete(request, id):
    assert isinstance(request, HttpRequest)
    role_droit = RoleDroit.objects.get(pk=id)
    role_droit.delete()
    messages.success(request, "Le RoleDroit a été Supprimé avec Succes !")
    return redirect('/roles_droits')