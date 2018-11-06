# Create your tests here.

from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from caesar.views.home import home_page

class HomePageTest(TestCase):

    '''resolve is the function Django uses internally to resolve URLs and find what view function they should map to.
    We’re checking that resolve, when called with “/”, the root of the site, finds a function called home_page.'''
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
