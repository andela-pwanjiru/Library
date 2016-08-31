from django.forms import ModelForm
from main.models import Book, Category


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'category']
