from django.shortcuts import render

# Create your views here.
from vocabulary.models import Vocabulary

def index(request):
    vocabs = Vocabulary.objects.all()
    context = {
        'vocabs': vocabs
    }
    print(context)
    # print(context.vocabs)
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')