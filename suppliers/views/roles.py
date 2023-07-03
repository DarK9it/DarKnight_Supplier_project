from django.shortcuts import redirect,render
from django.http import HttpRequest
from suppliers.models import Role
from suppliers.forms import RoleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#@login_required(login_url= "/login")
def index(request):
    assert isinstance(request, HttpRequest)
    roles = Role.objects.all()
    return render(
        request,
        'app/roles/index.html',
        {
            'roles': roles
        }
    )

#@login_required(login_url= "/login")   
def create(request):
    form = RoleForm()
    return render(
        request,
        'app/roles/create.html',
        {
            'form' : form
        }
    )
    
#@login_required(login_url= "/login")   
def store(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        nom = request.POST['nom']
        if Role.objects.filter(nom=nom).exists():
            messages.error(request, 'Un Role avec ce nom existe déjà.')
            return redirect('/roles')

        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enregistrer Avec Succes !")
    #retour a la page
    return redirect('/roles')


#@login_required(login_url= "/login")
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = RoleForm()
        else:
            role = Role.objects.get(pk=id)
            form = RoleForm(instance=role)
        return render(
            request,
            'app/roles/edit.html',
            {
                'form': form
            }
        )
        
        
# Update a Role
#@login_required(login_url= "/login")
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = RoleForm(request.POST)
        else:
            role = Role.objects.get(pk=id)
            form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
        messages.success(request, "Le Role a été Modifié avec Succes !")
        return redirect('/roles')
    

# Remove a Role
#@login_required(login_url= "/login")    
def delete(request, id):
    assert isinstance(request, HttpRequest)
    role = Role.objects.get(pk=id)
    role.delete()
    messages.success(request, "Le Role a été Supprimé avec Succes !")
    return redirect('/roles')