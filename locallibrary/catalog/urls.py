from django.urls import path

from .views import views
from .views import books
from .views import author

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('books/', books.BookListView.as_view(), name='books'),
    path('book/<int:pk>', books.BookDetailView.as_view(), name='book_detail'),
]

urlpatterns += [
    path('author/', author.AuthorListView.as_view(), name= 'author'),
    path('author/<int:pk>', author.AuthorDetailView.as_view(), name='author-detail')
]