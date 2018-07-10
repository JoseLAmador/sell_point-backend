from .models import Provider
from .serializers import ProviderSerializer, EditProviderSerializer
from rest_framework import viewsets
from .pagination import ProviderPagination


class ProviderViewFilterSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    pagination_class = ProviderPagination

    def get_serializer_class(self):
        if self.action == 'update':
            return EditProviderSerializer
        if self.action == 'partial_update':
            return EditProviderSerializer

        return ProviderSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Provider.objects.filter(owner=user)
