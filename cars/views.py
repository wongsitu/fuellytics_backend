from books.models import Book
from rest_framework import viewsets, filters
from books.serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from books.filters import CarFilter
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class Cars(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer
    
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['isbn', 'title', 'author', 'year']
    filter_class = CarFilter