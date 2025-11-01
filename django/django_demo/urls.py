from django.contrib import admin
from django.urls import path, include
from book_store import views

urlpatterns = [
    path('', views.home, name='home'),  # optional homepage
    path('books/', include('book_store.urls')),  # include your app’s URLs
    path('admin/', admin.site.urls),
]
