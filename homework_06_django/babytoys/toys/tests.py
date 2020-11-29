from django.test import TestCase
from .models import Category


class TestCategories(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Деревянные игрушки")

    def tearDown(self):
        pass

    def test_str(self):
        self.assertEqual(str(self.category), "Деревянные игрушки")
