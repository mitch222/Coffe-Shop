from django.test import TestCase
from django.urls import reverse

from products.models import Product

# Create your tests here.
class ProductsListViewTests(TestCase):
    def test_products_list_view_status_code(self):
        url = reverse('list_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_products_list_view_with_product(self):
        url = reverse('list_products')
        Product.objects.create(name="Test Product", price=10.0)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1)
        
    