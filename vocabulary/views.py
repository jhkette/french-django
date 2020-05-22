from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Vocabulary


def index(request):
    html = "<html>hello</html>" 
    return HttpResponse(html)
  

def vocabulary(request, vocabulary_id):
    vocabs = get_object_or_404(Vocabulary, pk=vocabulary_id)
    context = {
        'vocabs': vocabs
    }
    return render(request, 'vocabulary/vocabulary.html', context)


def search(request):
    html = "<html>search</html>" 
    return HttpResponse(html)