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


class HomePageButtonLinkTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def assertButtonLinksTo(self, url_name, button_text):
        url = reverse(url_name)
        onclick_snippet = f"onclick=\"location.href='{url}'\""
        msg = f"Button “{button_text}” should link to URL named '{url_name}'"
        self.assertContains(self.response, onclick_snippet, msg_prefix=msg)

    def test_meal_prep_button(self):
        self.assertButtonLinksTo('prep', 'Meal Prep')

    def test_grocery_list_button(self):
        self.assertButtonLinksTo('grocery', 'Grocery list')

    def test_quick_meal_ideas_button(self):
        self.assertButtonLinksTo('quick', 'Quick Meal Ideas')

    def test_bakes_button(self):
        self.assertButtonLinksTo('bakes', 'Bakes')

    def test_lunch_dinner_button(self):
        self.assertButtonLinksTo('lunch', 'Lunch/Dinner')

    def test_desserts_button(self):
        self.assertButtonLinksTo('desserts', 'Desserts')

    def test_about_us_button(self):
        self.assertButtonLinksTo('about', 'About Us')

