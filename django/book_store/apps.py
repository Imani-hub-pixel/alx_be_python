from django.apps import AppConfig

class BookStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_store'

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the ALX Book Store 📚")
