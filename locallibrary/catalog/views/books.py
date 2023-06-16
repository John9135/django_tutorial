from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from ..models.book import Book

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

    def get_context_date(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_date']= 'This is just some data'
        return context
    
class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})