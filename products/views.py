from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Product
from .forms import ProductForm
# Create your views here.
class ProductFormView(generic.FormView):
    # se requiere el template_name
    template_name = 'products/add_product.html'
    # Se tiene que importar el formulario
    form_class = ProductForm
    #

    success_url =  reverse_lazy('add_product')#'/products/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'    # Cambiar el nombre de la variable que se pasa al template
    
    #def get_queryset(self):
    #    return Product.objects.all()