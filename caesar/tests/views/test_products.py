# Create your tests here.

from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from caesar.views.products import products_page
from caesar.urls import products

from unittest import mock

from django.contrib.messages.storage.fallback import FallbackStorage
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from caesar.tests.factories.product import ProductFactory


class ProductPageTest(TestCase):

    '''resolve is the function Django uses internally to resolve URLs and find what view function they should map to.
    We’re checking that resolve, when called with “/”, the root of the site, finds a function called home_page.'''
    def test_url_resolves_products_page_view(self):
        found = resolve('/products/list')
        self.assertEqual(found.func, products_page)

    def test_products_page_returns_correct_html(self):
        response = self.client.get('/products/list')
        self.assertTemplateUsed(response, 'products.html')

    @mock.patch('django.shortcuts.render')
    def test_product_page_list(self, mock_render):
        request_factory = RequestFactory()

        ProductFactory(name='Product mocktest 1')
        ProductFactory(name='Product mocktest 2')

        request = request_factory.get(reverse('products:products_list'))
        products_page(request)
        from django.shortcuts import render
        self.assertEqual(render,mock_render)
        self.assertTrue(mock_render.called)
        request, template, context = mock_render.call_args[0]
        self.assertEqual(template, 'products.html')
        self.assertEqual(len(context['products']), 2)


