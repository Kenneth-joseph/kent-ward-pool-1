from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.
#testing home page status code

# class HomePageTest(SimpleTestCase):
#     def test_homepage_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_homepage_urls_name(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
    
#     def test_homepage_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'home.html')

class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! i shouldnt be in the page. '
        )
