from django.db import models
from .book import Book
import uuid


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique ID for this particular book across whole library')
    #uniqueld = models.CharField(max_length=50)
    due_back = models.DateField(null=True, blank=True)
    imprint = models.CharField(max_length=200)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    #borrower = models.ForeignKey('', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('m','Maintance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status_exact = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    class Meta:
        ordering = ['due_back']


    def __str__(self):
        return f'{self.id}({self.book.title})'