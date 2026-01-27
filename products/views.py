from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from products.forms import ProductForm
from products.models import Product

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'    