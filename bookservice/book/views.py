from rest_framework import generics, permissions

from .models import Book
from .renderers import OutBoundDataRenderer
from .serializers import BookModelSerializer


class BookListAPIView(generics.ListCreateAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (OutBoundDataRenderer,)


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (OutBoundDataRenderer,)
    lookup_field = 'id'
