from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,null= True, blank =True)
    nombre = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.nombre   

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null= True)
    precio = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url =''
        return url


class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete =models.SET_NULL, null=True, blank=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completa = models.BooleanField(default=False, null=True, blank= False)
    transaction_id = models.CharField(max_length=200, null= True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_carro(self):
        ordenitem = self.ordenproducto_set.all()
        total = sum([item.get_total for item in ordenitem])
        return total
    @property
    def get_total_item(self):
        ordenitem = self.ordenproducto_set.all()
        total = sum([item.cantidad for item in ordenitem])
        return total 
    

class OrdenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agrega = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total


class DireccionEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete =models.SET_NULL, null=True, blank=True)
    orden = models.ForeignKey(Orden, on_delete =models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200, null= True)
    ciudad = models.CharField(max_length=200, null= True)
    region = models.CharField(max_length=200, null= True)
    codigopostal = models.CharField(max_length=200, null= True)
    fecha_agrega = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion




   





    

