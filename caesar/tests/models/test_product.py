
from django.test import TestCase
from caesar.models.product import Product
from caesar.tests.factories.product import ProductFactory


class ProductTest(TestCase):

    def setUp(self):
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()
        self.product_1.save()
        self.product_2.save()

    def test_retrieving_product(self):

        saved_products = Product.objects.all()
        self.assertEqual(saved_products.count(), 2)

        first_saved_product = saved_products[0]
        second_saved_product = saved_products[1]
        self.assertEqual(first_saved_product.name, self.product_1.name)
        self.assertEqual(second_saved_product.name, self.product_2.name)