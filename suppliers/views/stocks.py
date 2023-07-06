from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from suppliers.models import Stock
from suppliers.forms import StockForm
from django.contrib.auth.decorators import  login_required

@login_required(login_url='/login')

def index(request):
    assert isinstance(request, HttpRequest)
    stocks = Stock.objects.all()
    return render(
        request,
        'app/stocks/index.html',
        {
            'stocks': stocks
        }
    )
@login_required(login_url='/login')

def create(request):
    form = StockForm()
    return render(
        request, 
        'app/stocks/create.html',
        {
            'form': form
        }
    )
@login_required(login_url='/login')

def store(request):
    if request.method == 'POST':
        nom = request.POST['produit']

        if Stock.objects.filter(produit_id=nom).exists():
            messages.error(request, 'Un produit avec le même nom existe déjà dans le stock.')
            return redirect('/stocks')

        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Stock has been saved successfully !")
        return redirect('/stocks')

@login_required(login_url='/login')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = StockForm()
        else:
            stock = Stock.objects.get(pk=id)
            form = StockForm(instance=stock)
        return render(
            request,
            'app/stocks/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = StockForm(request.POST)
        else:
            stock = Stock.objects.get(pk=id)
            form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
        messages.success(request, "Stock has been updated successfully !")
        return redirect('/stocks')

@login_required(login_url='/login')

def delete(request, id):
    stock = Stock.objects.get(pk=id)
    stock.delete()
    messages.success(request, "Stock has been removed successfully !")
    return redirect('/stocks')