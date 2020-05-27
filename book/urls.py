from django.urls import path, include


from . import views
urlpatterns  = [
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    # path('<int:listing_id>', views.listing, name = "listing"),
    # path('search', views.search, name = "search")
]