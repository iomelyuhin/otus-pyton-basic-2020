from django.test import TestCase, Client
from .models import Category, Card


class TestCategories(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Деревянные игрушки")

    def tearDown(self):
        print('Done')

    def test_str(self):
        self.assertEqual(str(self.category), "Деревянные игрушки")


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Деревянные игрушки")

    def tearDown(self):
        print('Done')

    def test_index_menu(self):
        response = self.client.get("")
        text = response.content.decode(encoding='utf-8')
        self.assertTrue(str(self.category) in text)

    def test_index_context(self):
        response = self.client.get("")
        self.assertTrue('categories' in response.context)
