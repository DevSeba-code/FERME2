from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as do_logout
from django.contrib import messages  # import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm  # add this
import json

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form' : form}
    return render (request, 'app1/register.html', context)

def shop(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        order , created = Orden.objects.get_or_create(cliente=cliente , completa=False)
        items = order.ordenproducto_set.all()
        carroItem = order.get_total_item

    else:
        items = []
        order = {'get_total_carro':0 ,'get_total_item':0}
        carroItem =order['get_total_carro']

    productos = Producto.objects.all()
    context = {'productos':productos ,'carroItem':carroItem}
    return render(request, 'app1/shop.html', context)

def cart(request):
    #descomentar esto para validar que este authenticado
    if request.user.is_authenticated:
        cliente = request.user.cliente
        order, created = Orden.objects.get_or_create(cliente=cliente, completa=False)
        items = order.ordenproducto_set.all()
        carroItem = order.get_total_item
    else: 
        items = []
        order = {'get_total_carro':0,'get_cart_items':0}
        carroItem =order['get_total_carro']
    context = {'items':items, 'orden':order,'carroItem':carroItem}

    return render(request, 'app1/cart.html', context)


def contact(request):
    context = {}
    return render(request, 'app1/contact.html', context)

def about(request):
    context = {}
    return render(request, 'app1/about.html', context)



# def carrito(request):
# 	context = {}
# 	return render(request, 'app1/carrito.html', context)

def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        order , created = Orden.objects.get_or_create(cliente=cliente , completa=False)
        items = order.ordenproducto_set.all()
    else:
        items = []
        order = {'get_total_carro':0 ,'get_cart_items':0}
    context = {'items':items , 'orden' : order}
    return render(request,'app1/checkout.html', context)



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = NewUserForm()
    return render(request, 'app1/register.html', {'register_form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="app1/login.html", context={"login_form": form})


def logout_request(request):
    do_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def home(request):
    return render(request, 'app1/index.html')


def vista_cli_home(request):
    return render(request, 'app1/vista-cli-general.html')


def updateProducto(request):
    data = json.loads(request.body)
    productoId = data['productoId']
    action = data['action']

    cliente= request.user.cliente
    producto = Producto.objects.get(id= productoId)
    order , created = Orden.objects.get_or_create(cliente=cliente , completa=False)
    orderItem, created = OrdenProducto.objects.get_or_create(orden=order , producto=producto)

    if action== 'add':
        orderItem.cantidad= (orderItem.cantidad + 1)
    elif action=='remove':
        orderItem.cantidad= (orderItem.cantidad - 1)
    
    orderItem.save()

    if orderItem.cantidad <= 0 :
        orderItem.delete()

    return JsonResponse('El producto fue agregado',safe=False)