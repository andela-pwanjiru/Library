from django.conf.urls import url
from main.views import LibraryView

urlpatterns = [
    url(r'^', LibraryView.as_view(), name='search'),
]