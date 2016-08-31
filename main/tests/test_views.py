from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from main.models import Book, Category


class TestLibraryView(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Fantasy')
        self.book = Book.objects.create(title='How to get married', category=self.category)

    def test_search_by_name(self):
        response = self.client.get(reverse('search'), self.book)
        self.assertEquals(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_for_nonexisting_book(self):
        url = reverse('search')
        book = {'title': 'exist'}
        response = self.client.get(url, book)
        self.assertEquals(response.status_code, 404)

    def test_search_by_category(self):
        response = self.client.get(reverse('search'), self.category)
        self.assertEquals(response.status_code, 200)

    def test_search_with_nonexisting_category(self):
        url = reverse('search')
        category = {'name': 'none'}
        response = self.client.get(url, category)
        self.assertEquals(response.status_code, 404)
