from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse

class BlogTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_contacts(self):
        response = self.client.get(reverse("contacts"))
        exp_data = "Контактная информация"
        self.assertEqual(exp_data, response.content.decode())

    def test_about(self):
        response = self.client.get(reverse("about"))
        exp_data = "О нас"
        self.assertEqual(exp_data, response.content.decode())

    def test_main(self):
        response = self.client.get(reverse("index-page"))
        exp_data = "Main page"
        self.assertEqual(exp_data, response.content.decode())

    def test_test_page(self):
        response = self.client.get(reverse("test-page"))
        exp_data = "Test"
        self.assertEqual(exp_data, response.content.decode())
        self.assertEqual(response.status_code, 404)