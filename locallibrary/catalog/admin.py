from django.contrib import admin

# Register your models here.
from .models.author import Author
from .models.book import Book
from .models.book_Instance import BookInstance
from .models.genre import Genre
from .models.language import Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status_exact', "due_back")

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status_exact', 'due_back')
        })
    )

admin.site.register(Genre)
admin.site.register(Language)