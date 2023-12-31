from django.shortcuts import render

from ..models.author import Author
from ..models.book import Book
from ..models.book_Instance import BookInstance
from ..models.genre import Genre
from ..models.language import Language



def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status_exact='a').count()
    num_authors = Author.objects.count()

    count = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available':num_instances_available,
        'num_authors': num_authors,
    }

    return render(
        request, 
        'catalog/index.html', 
        context={
            'context': count
        }
    )
