from django.contrib.auth.models import User
from .models import Income
from .serializers import IncomeSerializer, UserSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer