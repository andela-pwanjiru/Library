from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from main.models import Book, Category


class TestLibraryView(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Fantasy')
        self.book = Book.objects.create(title='How to get married', category=self.category)

    def test_search_by_name(self):
        book = {'title': 'name'}
        response = self.client.get(reverse('search'), book)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_by_category(self):
        category = {'name': 'cooking'}
        response = self.client.get(reverse('search'), category)
        self.assertEquals(response.status_code, 200)
