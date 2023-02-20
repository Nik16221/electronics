from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from product_info.models import Products, Contacts, Sales
from product_info.serializers import ContactsSerializer, ProductsSerializer, SalesSerializers


class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer


class ContactsView(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContactsSerializer


class SalesView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SalesSerializers

    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['country']
