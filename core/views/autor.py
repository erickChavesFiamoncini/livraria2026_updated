from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
