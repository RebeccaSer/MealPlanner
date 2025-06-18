from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'meals/home.html')

    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Mokone Meal Diaries')

