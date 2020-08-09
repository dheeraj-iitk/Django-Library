from django.shortcuts import render
from catalog.models import Books, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    num_books=Books.objects.all().count()
    num_instances=BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView): #this view by default passes the books list
    model = Books
    template_name = 'book_list.html'
    paginate_by=2

  #  def get_queryset(self):
     #   return Books.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(generic.DetailView):
    model = Books
    template_name='book_detail.html'

class AuthorListView(generic.ListView):
    model=Author
    template_name='author_list.html'

class AuthorDetailView(generic.DetailView):
    model=Author
    template_name='author_detail.html'

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
   # """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')