from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomepageView


class HomepageTests(TestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")
        
    def test_hompage_contains_correct_html_code(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html_code(self):
        self.assertNotContains(self.response, "Login")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomepageView.as_view().__name__,
        )
        

# Create your tests here.
