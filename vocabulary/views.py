from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Vocabulary

def vocabulary(request, listing_id):
    listing = get_object_or_404(Vocabulary, pk=vocabulary_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)