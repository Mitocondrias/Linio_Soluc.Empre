from django.db import models

class Proveedor(models.Model):
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)


class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)


class Localizacion(models.Model):
    distrito = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)

class Producto(models.Model):
    # Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # Atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.CharField(max_length=3)
    descuento = models.FloatField(default=0)

    def precio_final(self):
        return self.precio * (1 - self.descuento)

    def sku(self):
      codigo_categoria = self.categoria.codigo.zfill(4)
      codigo_producto = str(self.id).zfill(6)

      return f'{codigo_categoria}-{codigo_producto}'

class Pedido(models.Model):
    #Relaciones
    ubicacion = models.ForeignKey('Localizacion', on_delete=models.SET_NULL, null=True)
    
    #Atributos
    fechaCreacion = models.DateField()
    estado = models.TextField()
    fechaEntrega = models.DateField()
    direccionEntrega = models.TextField()
    tarifa = models.FloatField(default=0)

    def calcular_tarifa(self):
        return self.tarifa

    def listar_pedidos_estado(self):
        return self.estado

    def asignar_repartidor(self):
        return self.repartidor

    
class DetallePedido(models.Model):
    #Relaciones
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)

    #Atributos
    cantidad = models.IntegerField()
    subtotal = models.FloatField()

    def calcular_subtotal(self):
        return self.subtotal