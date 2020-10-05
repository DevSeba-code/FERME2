from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200, null= True)
    apellido = models.CharField(max_length=200, null= True)
    def __str__(self):
        return self.nombre   

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null= True)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete =models.SET_NULL, null=True, blank=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completa = models.BooleanField(default=False, null=True, blank= False)
    transaction_id = models.CharField(max_length=200, null= True)

    def __str__(self):
        return str(self.id)

class OrdenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete =models.SET_NULL, null=True, blank=True)
    orden = models.ForeignKey(Orden, on_delete =models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=0, null= True, blank = True)
    fecha_agrega = models.DateTimeField(auto_now_add=True)
# class Cliente(models.Model):
#     id_cli= models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30, null=True)
#     password = models.CharField(max_length=30, null=True)
#     nombre = models.CharField(max_length=50, null=True)
#     apellido = models.CharField(max_length=50, null=True)
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
#     direccion = models.CharField(max_length=30, null=True)
#     rut = models.CharField(max_length=30, null=True)
#     telefono = models.IntegerField(12)
#     email = models.CharField(max_length=100, null=True)
#     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE)
#     id_factura = models.ForeignKey('Factura',on_delete=models.CASCADE)
#     id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE)
#     id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)


# class Empleado(models.Model):
#     id_empleado = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30, null =True)
#     password = models.CharField(max_length=30, null =True)
#     nombre = models.CharField(max_length=50, null =True)
#     apellido = models.CharField(max_length=50, null =True)
#     direccion = models.CharField(max_length=30, null =True)
#     rut = models.CharField(max_length=30, null =True)
#     id_cargo = models.ForeignKey('Tipo_Emp', on_delete=models.CASCADE)
#     id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)


# class Tipo_Emp(models.Model):
#     id_cargo = models.AutoField(primary_key=True)
#     cargo = models.CharField(max_length=30, null =True)
#     id_boleta = models.ForeignKey('Boleta', on_delete=models.CASCADE)
#     id_factura = models.ForeignKey('Factura',on_delete=models.CASCADE)
#     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE)
#     id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
# class Proveedor(models.Model):
#     id_prove = models.AutoField(primary_key=True) 
#     nombre = models.CharField(max_length=30, null =True)
#     rut_empresa = models.CharField(max_length=30, null =True)
#     rubro = models.CharField(max_length=30, null =True)
#     id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
#     id_factura = models.ForeignKey('Factura',on_delete=models.CASCADE)
#     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE) 
 
# class Pedido(models.Model):
#     id_pedido = models.AutoField(primary_key=True) 
#     estado_recep = models.CharField(max_length=30, null =True)
#     id_prove = models.ForeignKey('Proveedor',on_delete=models.CASCADE)
#     id_cli = models.ForeignKey('Cliente',on_delete=models.CASCADE)
#     id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
#     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE)

# class Boleta(models.Model):
#     id_boleta = models.AutoField(primary_key=True) 
#     fecha_emision = models.DateTimeField(auto_now_add=True)
#     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE)
#     id_pedido = models.ForeignKey('Pedido',on_delete=models.CASCADE)
#     id_cli = models.ForeignKey('Cliente',on_delete=models.CASCADE)

# class Factura(models.Model):
#     id_factura = models.AutoField(primary_key=True)
#     id_producto = models.ForeignKey('Producto',on_delete=models.CASCADE)
#     id_pedido = models.ForeignKey('Pedido',on_delete=models.CASCADE)
#     id_cli = models.ForeignKey('Cliente',on_delete=models.CASCADE)

# class Producto(models.Model):
#     id_producto = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=30, null =True)
#     precio = models.IntegerField(8)
#     stock = models.IntegerField(10)
#     disponibilidad = models.BooleanField(default=True)
#     familia = models.CharField(max_length=30, null =True)
#     fecha_ven = models.DateField(null = True, blank=True)
#     descripcion = models.CharField(max_length=30, null =True)

   





    

