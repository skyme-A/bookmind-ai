from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class BookSummaryView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return Response({
            "summary": book.summary
        })


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRecommendationView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        book = Book.objects.get(pk=self.kwargs['pk'])
        return Book.objects.filter(genre=book.genre).exclude(id=book.id)