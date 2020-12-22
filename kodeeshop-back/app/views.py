from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from rest_framework import status
from rest_framework import views
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app import serializers
from app.cores.message import Message
from app.models.collection import Collection
from app.models import Tag, Customer, CustomerShipment, Product


class CustomerListView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.CustomerCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            first_name = data.get('first_name') if data.get('first_name') else None
            last_name = data.get('last_name') if data.get('last_name') else None
            email = data.get('email') if data.get('email') else None
            password = data.get('password') if data.get('password') else None
            birthday = data.get('birthday') if data.get('birthday') else None
            phone = data.get('phone') if data.get('phone') else None
            gender = data.get('gender') if data.get('gender') else None
            customer_shipment = data.get('customer_shipment') if data.get('customer_shipment') else None

            customer = Customer.objects.get_customer_by_email_or_phone(email, phone)
            if customer:
                return Response(Message.DATA_DUPLICATE, status.HTTP_200_OK)

            if customer_shipment:
                if not customer_shipment.get('first_name') and first_name:
                    customer_shipment['first_name'] = first_name
                if not customer_shipment.get('last_name') and last_name:
                    customer_shipment['last_name'] = last_name
                if not customer_shipment.get('phone') and phone:
                    customer_shipment['phone'] = phone

            try:
                if customer_shipment:
                    customer_shipment = CustomerShipment.objects.create_customer_shipment(customer_shipment)

                customer_data_create = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': make_password(password),
                    'birthday': birthday,
                    'phone': phone,
                    'gender': gender,
                    'customer_shipment': customer_shipment if customer_shipment else None
                }
                Customer.objects.create_customer(customer_data_create)
                return Response(Message.CREATE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.CREATE_ERROR, status.HTTP_200_OK)

        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomerDetailView(views.APIView):

    def put(self, request, *args, **kwargs):
        serializer = serializers.CustomerUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            id_customer = self.kwargs.get('id_customer')
            first_name = data.get('first_name') if data.get('first_name') else None
            last_name = data.get('last_name') if data.get('last_name') else None
            email = data.get('email') if data.get('email') else None
            password = data.get('password') if data.get('password') else None
            birthday = data.get('birthday') if data.get('birthday') else None
            phone = data.get('phone') if data.get('phone') else None
            gender = data.get('gender') if data.get('gender') else None
            customer_shipment = data.get('customer_shipment') if data.get('customer_shipment') else None

            try:
                customer_update = Customer.objects.get_customer_by_id(id=id_customer)
                if not customer_update:
                    return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

                customer_data_update = {}
                if first_name and customer_update['first_name'] != first_name:
                    customer_data_update.update({
                        'first_name': first_name
                    })

                if last_name and customer_update['last_name'] != last_name:
                    customer_data_update.update({
                        'last_name': last_name
                    })

                if email and customer_update['email'] != email:
                    customer_data_update.update({
                        'email': email
                    })

                if password and customer_update['password'] != make_password(password):
                    customer_data_update.update({
                        'password': make_password(password)
                    })

                if birthday and customer_update['birthday'] != birthday:
                    customer_data_update.update({
                        'birthday': birthday
                    })

                if phone and customer_update['phone'] != phone:
                    customer_data_update.update({
                        'phone': phone
                    })

                if gender and customer_update['gender'] != gender:
                    customer_data_update.update({
                        'gender': gender
                    })

                if customer_shipment:
                    customer_shipment_data_update = {}
                    customer_shipment_update = CustomerShipment.objects.get_customer_shipment_by_id(
                        customer_update['customer_shipment_id'])
                    for key, value in customer_shipment.items():
                        if customer_shipment[key] != customer_shipment_update[key]:
                            customer_shipment_data_update.update({
                                key: value
                            })
                    Customer.objects.update_customer_by_id(data=customer_data_update, id=id_customer)
                    CustomerShipment.objects.update_customer_shipment_by_id(data=customer_shipment_data_update,
                                                                            id=customer_shipment_update['id'])
                return Response(Message.UPDATE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.UPDATE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        serializer = serializers.CustomerDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            id_customer = self.kwargs.get('id_customer')

            customer_delete = Customer.objects.get_customer_by_id(id_customer)
            if not customer_delete:
                return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

            try:
                Customer.objects.delete_customer_by_id(id_customer)
                return Response(Message.DELETE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.DELETE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)


class CollectionListView(views.APIView):

    def get(self, request, *args, **kwargs):
        serializer = serializers.CollectionListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            collection_list = Collection.objects.get_all_collection()
            if collection_list:
                return Response(collection_list, status.HTTP_200_OK)
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CollectionCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            name = data.get('name')
            slug = data.get('slug') if data.get('slug') else None

            if not slug:
                slug = slugify(name, allow_unicode=True)

            collection = Collection.objects.get_collection_by_slug(slug)
            if collection:
                return Response(Message.DATA_DUPLICATE, status.HTTP_200_OK)

            try:
                Collection.objects.create_collection(name=name, slug=slug)
                return Response(Message.CREATE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.CREATE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)


class CollectionDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        serializer = serializers.CollectionDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            id_collection = data.get('id_collection')

            collection = Collection.objects.get_collection_by_id(id_collection)
            if collection:
                return Response(collection, status.HTTP_200_OK)
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        serializer = serializers.CollectionUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            id_collection = self.kwargs.get('id_collection')
            name = data.get('name') if data.get('name') else None
            slug = data.get('slug') if data.get('slug') else None

            collection_update = Collection.objects.get_collection_by_id(id_collection)
            if not collection_update:
                return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

            if not slug:
                slug = slugify(name, allow_unicode=True)

            collection = Collection.objects.get_collection_by_slug(slug)
            if collection:
                return Response(Message.DATA_DUPLICATE, status.HTTP_200_OK)

            collection_data_update = {}
            if name and collection_update['name'] != name:
                collection_data_update.update({
                    'name': name
                })

            if collection_update['slug'] != slug:
                collection_data_update.update({
                    'slug': slug
                })

            try:
                Collection.objects.update_collection_by_id(data=collection_data_update, id=id_collection)
                return Response(Message.UPDATE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.UPDATE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        serializer = serializers.CollectionDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            id_collection = self.kwargs.get('id_collection')

            collection_delete = Collection.objects.get_collection_by_id(id_collection)
            if not collection_delete:
                return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

            try:
                Collection.objects.delete_collection_by_id(id_collection)
                return Response(Message.DELETE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.DELETE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)


@permission_classes((AllowAny,))
class TagListView(views.APIView):

    def get(self, request, *args, **kwargs):
        serializer = serializers.TagListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            tag_list = Tag.objects.get_all_tag()
            if tag_list:
                return Response(tag_list, status.HTTP_200_OK)
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CollectionCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            name = data.get('name')
            slug = data.get('slug') if data.get('slug') else None

            if not slug:
                slug = slugify(name, allow_unicode=True)

            tag = Tag.objects.get_tag_by_slug(slug)
            if tag:
                return Response(Message.DATA_DUPLICATE, status.HTTP_200_OK)

            try:
                Tag.objects.create_tag(name=name, slug=slug)
                return Response(Message.CREATE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.CREATE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)


class TagDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        serializer = serializers.TagDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            id_tag = data.get('id_tag')

            tag = Collection.objects.get_tag_by_id(id_tag)
            if tag:
                return Response(tag, status.HTTP_200_OK)
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        serializer = serializers.TagUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            data = serializer.data
            id_tag = self.kwargs.get('id_tag')
            name = data.get('name') if data.get('name') else None
            slug = data.get('slug') if data.get('slug') else None

            tag_update = Tag.objects.get_tag_by_id(id_tag)
            if not tag_update:
                return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

            if not slug:
                slug = slugify(name, allow_unicode=True)

            tag = Tag.objects.get_tag_by_slug(slug)
            if tag:
                return Response(Message.DATA_DUPLICATE, status.HTTP_200_OK)

            tag_data_update = {}
            if name and tag_update['name'] != name:
                tag_data_update.update({
                    'name': name
                })
            if tag_update['slug'] != slug:
                tag_data_update.update({
                    'slug': slug
                })

            try:
                Tag.objects.update_tag_by_id(data=tag_data_update, id=id_tag)
                return Response(Message.UPDATE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.UPDATE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        serializer = serializers.TagDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(Message.BAD_REQUEST, status.HTTP_400_BAD_REQUEST)

        try:
            id_tag = self.kwargs.get('id_tag')

            try:
                Tag.objects.delete_tag_by_id(id=id_tag)
                return Response(Message.DELETE_SUCCESS, status.HTTP_200_OK)
            except Exception as e:
                return Response(Message.DELETE_ERROR, status.HTTP_200_OK)
        except Exception as e:
            return Response(Message.ERROR_SERVER, status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductListView(views.APIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(id=1).values(
            'tag__name'
        )
        return Response(product, status.HTTP_200_OK)


class ProductDetailView(views.APIView):
    pass
