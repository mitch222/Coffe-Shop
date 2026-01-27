from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción", widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(required=False, initial=True, label="Disponible")
    photo = forms.ImageField(required=False, label="Foto")
    
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'])