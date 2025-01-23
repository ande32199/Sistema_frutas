from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    descripcion = models.TextField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)

class Ventas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Productos)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=8, decimal_places=2, default=0)