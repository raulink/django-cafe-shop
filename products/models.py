from django.db import models

# Create your models here.

# Si no detecta el entorno virtual se necesita inicializar 
class Product(models.Model):
    name = models.CharField(max_length=255,verbose_name='nombre')
    description = models.TextField(max_length=300, verbose_name='descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='precio')
    available = models.BooleanField(default=True,verbose_name='disponible')
    photo = models.ImageField(upload_to='products/photos/',verbose_name='foto',null=True,blank=True)
    
    def __str__ (self):
        return self.name