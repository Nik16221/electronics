from rest_framework import serializers
from product_info.models import Contacts, Products, Sales


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

    contacts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

#     # def validate_update_arrears_field(self, value):
#     #     if self.instance and value.id != self.instance.foo_id:
#     #         raise serializers.ValidationError("запрет на обновление")
#     #     return value
