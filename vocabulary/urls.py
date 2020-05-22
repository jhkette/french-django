from django.urls import path

from . import views
urlpatterns  = [
    path('', views.index, name = "vocabs"),
    path('<int:vocabulary_id>', views.vocabulary, name = "vocabulary"),
    path('search', views.search, name = "search")
]