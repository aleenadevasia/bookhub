from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, BookDeleteAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path('<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book-delete'),
]
