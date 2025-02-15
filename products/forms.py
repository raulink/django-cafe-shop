from django import forms

from products.models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100,label='Nombre')
    price = forms.DecimalField(max_digits=10, decimal_places=2,label='Precio')
    description = forms.CharField(widget=forms.Textarea, max_length=1000,label='Descripcion')
    available = forms.BooleanField(label='Disponible',initial=True,required=False)
    image = forms.ImageField(label='Imagen',required=False)
    category = forms.CharField(max_length=100)

    # Acciones cuando hagan submit, 
    # Guardar en la base de datos
    def save(self):
        data = self.cleaned_data    # Traer la informacion limpia cuando se hace request al formulario
        product = Product()
        product.name = data['name']
        product.price = data['price']
        product.description = data['description']
        product.available = data['available']
        product.image = data['image']
        product.category = data['category']
        product.save()

    # se puede hacer validaciones de los campos
