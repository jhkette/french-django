from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Book

def index(request):
    books = Book.objects.all().order_by('-list_date')
