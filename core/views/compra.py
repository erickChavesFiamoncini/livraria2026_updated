from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import (
    CompraCreateUpdateSerializer,
    CompraListSerializer,
    CompraSerializer,
)

# Dando erro na API por conta do usuário Anonymous

# class CompraViewSet(ModelViewSet):
# # queryset = Compra.objects.all()
# serializer_class = CompraSerializer

#   def get_queryset(self):
#      usuario = self.request.user
#     if usuario.is_superuser:
#        return Compra.objects.order_by('-id')
#   if usuario.groups.filter(name='administradores'):
#      return Compra.objects.order_by('-id')
# return Compra.objects.filter(usuario=usuario).order_by('-id')

# def get_serializer_class(self):
#   if self.action == 'list':
#      return CompraListSerializer
# if self.action in ('create', 'update', 'partial_update'):
#    return CompraCreateUpdateSerializer
# return CompraSerializer


class CompraViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user

        if usuario.is_superuser:
            return Compra.objects.order_by('-id')

        if usuario.groups.filter(name='administradores').exists():
            return Compra.objects.order_by('-id')

        return Compra.objects.filter(usuario=usuario).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return CompraListSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return CompraCreateUpdateSerializer

        return CompraSerializer
