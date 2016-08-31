from django.shortcuts import render
from django.views.generic import View
from main.forms import BookForm
from main.models import Book, Category

# Create your views here.
class LibraryView(View):
    def get(self, request):
        if request.GET:
            form = BookForm(request.GET)
            if form.is_valid():
                # import ipdb; ipdb.set_trace()
                book_name = form.cleaned_data.get('title')
                category_name = form.cleaned_data.get('category')
                if book_name:
                    object_list = Book.objects.filter(title__icontains=book_name)
                if category_name:
                    cat_obj = Category.objects.filter(name=category_name)
                    object_list = Book.objects.filter(category=cat_obj)
                form = {'object_list': object_list}
                return render(request, 'results.html', form)
        form = {'form': BookForm}
        return render(request, 'search.html', form)
