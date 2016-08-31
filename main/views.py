from django.shortcuts import render
from django.views.generic import View
from main.forms import BookForm

# Create your views here.
class LibraryView(View):
    def get(self, request):
        form = BookForm(request.GET)
        if form.is_valid():
            title = request.GET('title')
            category = request.GET('category')
            if title:
                object_list = Book.objects.filter(title_icontains=title)
            if category:
                object_list = Book.objects.filter(category=category)
            form = {'object_list': object_list}
            return render(request, 'results.html', form)

        context = {'form': form}
        return render(request, 'search.html', context)
