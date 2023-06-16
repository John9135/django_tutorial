from django.db import models
from django.urls import reverse

from .author import Author
from .genre import Genre
from .language import Language


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)


    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
