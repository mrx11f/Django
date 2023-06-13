from django.test import TestCase, Client
from django.urls import reverse

class BlogTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_contacts(self):
        response = self.client.get(reverse("contacts"))
        exp_data = "Контактная информация"
        self.assertEqual(exp_data, response.content.decode())

    def test_contacts(self):
        response = self.client.get(reverse("about"))
        exp_data = "О нас"
        self.assertEqual(exp_data, response.content.decode())