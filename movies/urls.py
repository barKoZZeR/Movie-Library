from django.urls import path
from .views import MovieListCreate, MovieRetrieveUpdateDestroy, edit_movie, add_movie, home, add_comment

urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
    path('movies/<int:pk>/edit/', edit_movie, name='edit_movie'),
    path('movies/<int:pk>/comments/add/', add_comment, name='add_comment'),
    path('', home, name='home'),
    path('add/', add_movie, name='add_movie'),
]