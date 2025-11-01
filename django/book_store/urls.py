from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # show homepage for /books/
    path('list/', views.book_list, name='book_list'),  # example route
]
