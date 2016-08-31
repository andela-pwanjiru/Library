from django.forms import ModelForm
from main.models import Book, Category


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['title'].required = False

    class Meta:
        model = Book
        fields = ['title', 'category']
