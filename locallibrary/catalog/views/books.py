from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from ..models.book import Book

class BookListView(generic.ListView):
    model = Book

    def get_context_date(self, **kwargs):
       def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5]
    
class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})