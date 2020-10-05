
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CrearFormUsuario

# Create your views here.


  # add this


def loginPage(request):
    if request.method == 'POST':
      username =  request.POST.get('username')
      password=  request.POST.get('password')
      
      user = authenticate(request, username=username, password=password)

      if user is not None:
          login(request,user)
          return redirect('home')
      else:
          messages.info(request, 'Nombre de usuario o contraseña incorrectos')
          
          

    
    context = {}
    return render(request, 'app1/login.html', context)

    


def registerPage(request):
    form = CrearFormUsuario()

    if request.method == 'POST':
        form = CrearFormUsuario(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request, user + ' tu cuenta ha sido creada con exito')
            
            return redirect('login')

    context = {'form': form}
    return render(request, 'app1/register.html', context)
    


def shop(request):
    context = {}
    return render(request, 'app1/shop.html', context)

def cart(request):
    context = {}
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
	context = {}
	return render(request, 'app1/checkout.html', context)
	




def home(request):
    return render(request, 'app1/index.html')


def vista_cli_home(request):
    return render(request, 'app1/vista-cli-general.html')
