from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import MovieSerializer
from .models import Movie
from .permissions import PermissionsClass

# Create your views here.
class MoviesListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (PermissionsClass,IsAuthenticated)

class MovieDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (PermissionsClass,IsAuthenticated)