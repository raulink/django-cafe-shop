from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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
