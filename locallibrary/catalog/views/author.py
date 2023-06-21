from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from ..models.author import Author

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'

    def get_context_date(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_date']= 'This is just some data'
        return context
    
class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})