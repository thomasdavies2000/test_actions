from django.test import TestCase
from .models import Genre
# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.catalog = Genre.objects.create(name="Science fiction")

    def test_genre_model(self):
        d = self.catalog
        self.assertTrue(isinstance(d, Genre))
