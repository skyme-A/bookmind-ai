from django.urls import path
from .views import BookListCreateView, BookDetailView, BookRecommendationView, BookSummaryView

urlpatterns = [
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/<int:pk>/recommend/', BookRecommendationView.as_view()),
    path('books/<int:pk>/summary/', BookSummaryView.as_view()),
]