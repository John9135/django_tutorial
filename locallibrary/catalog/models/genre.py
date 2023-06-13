from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book (e.g. science fiction)')

    def __str__(self):
        return self.name