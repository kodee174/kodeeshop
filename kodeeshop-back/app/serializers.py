from rest_framework import serializers
from app.models.customer import CustomerGender
from app.models.customer_shipment import CustomerCountry, CustomerCity, CustomerDistrict


class CustomerShipmentListSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    address = serializers.CharField(required=True)
    phone = serializers.CharField(required=False)
    country = serializers.ChoiceField(
        choices=CustomerCountry.choices,
        required=False
    )
    city = serializers.ChoiceField(
        choices=CustomerCity.choices,
        required=False
    )
    district = serializers.ChoiceField(
        choices=CustomerDistrict.choices,
        required=False
    )

class CustomerListSerializer(serializers.Serializer):
    pass


class CustomerCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=True)
    birthday = serializers.DateField(required=False)
    phone = serializers.CharField(required=True)
    gender = serializers.ChoiceField(
        choices=CustomerGender.choices,
        default=CustomerGender.Male,
        required=False
    )
    customer_shipment = CustomerShipmentListSerializer(required=False)


class CustomerUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    phone = serializers.CharField(required=False)
    gender = serializers.ChoiceField(
        choices=CustomerGender.choices,
        required=False
    )
    customer_shipment = CustomerShipmentListSerializer(required=False)


class CustomerDeleteSerializer(serializers.Serializer):
    pass

class CollectionListSerializer(serializers.Serializer):
    pass


class CollectionDetailSerializer(serializers.Serializer):
    id_collection = serializers.IntegerField(required=True)


class CollectionCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=False)


class CollectionUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)


class CollectionDeleteSerializer(serializers.Serializer):
    pass


class TagListSerializer(serializers.Serializer):
    pass


class TagDetailSerializer(serializers.Serializer):
    id_collection = serializers.IntegerField(required=True)


class TagCreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=False)


class TagUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)


class TagDeleteSerializer(serializers.Serializer):
    pass


class ProductListSerializer(serializers.Serializer):
    pass


class ProductDetailSerializer(serializers.Serializer):
    id_product = serializers.IntegerField(required=True)
