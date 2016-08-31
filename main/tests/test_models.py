from django.test import TestCase
from main.models import Book, Category
# Create your tests here.

class TestLibraryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Fantasy')
        self.book = Book.objects.create(title='How to get married', category=self.category)

    def test_book_can_be_created(self):
        self.assertIn('How to get married', Book.objects.get(title='How to get married').title)
        self.assertIsInstance(self.book, Book)

    def test_category_can_be_created(self):
        self.assertIn('Fantasy', Category.objects.get(name='Fantasy').name)
        self.assertIsInstance(self.category, Category)
