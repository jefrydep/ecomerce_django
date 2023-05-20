from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.

User= get_user_model() #devuelve el usuario logueado actual


class Pedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.id

    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total= Sum(F("Precio")*F("camtidad"), output_field=FloatField())

        )["total"]

    class Meta:
        db_table= "pedidos"
        verbose_name= "pedido"
        verbose_name_plural="pedidos"
        ordering=['id']

class LineaPedido(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    pedido_id=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad= models.IntegerField(default=1)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str___(self):
        return f"{self.cantidad} unidades de {self.producto_id.nombre}"

    class Meta:
        db_table= "lineapedidos"
        verbose_name= "lineapedido"
        verbose_name_plural="lineapedidos"
        ordering=['id']
