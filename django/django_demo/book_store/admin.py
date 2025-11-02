from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # columns shown in list view
    search_fields = ('title', 'author')                   # adds a search bar
    list_filter = ('published_date',)                     # adds sidebar filter
