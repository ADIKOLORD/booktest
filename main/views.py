from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookAPIViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
