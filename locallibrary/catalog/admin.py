from django.contrib import admin
from .models import Author,Genre,Books,BookInstance

#admin.site.register(Books)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author,AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model=BookInstance
    extra=0

# Register the Admin classes for Book using the decorator
class BooksAdmin(admin.ModelAdmin):
    list_display=('title','author','display_genre')
    inlines=[BooksInstanceInline]
admin.site.register(Books,BooksAdmin)

# Register the Admin classes for BookInstance using the decorator
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('__str__','status','borrower','due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
admin.site.register(BookInstance,BookInstanceAdmin)

