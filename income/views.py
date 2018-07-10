from django.contrib.auth.models import User
from .models import Income, Cliente
from .serializers import IncomeSerializer, UserSerializer, ClienteSerializer, EditClienteSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from .pagination import ClientePagination


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = ClientePagination

class ClienteViewFilterSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    pagination_class = ClientePagination

    def get_serializer_class(self):
        if self.action == 'update':
            return EditClienteSerializer
        if self.action == 'partial_update':
            return EditClienteSerializer

        return ClienteSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Cliente.objects.filter(owner=user)


