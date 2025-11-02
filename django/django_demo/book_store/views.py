
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Welcome back to my book store")

# Create your views here.
