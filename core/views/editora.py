from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from core.models import Editora
from core.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.order_by('nome')
    serializer_class = EditoraSerializer
