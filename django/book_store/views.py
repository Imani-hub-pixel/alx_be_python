from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
