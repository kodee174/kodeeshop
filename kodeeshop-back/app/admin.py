from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.account import Account
from .models.customer import Customer
from .models.customer_shipment import CustomerShipment
from .models.collection import Collection
from .models.tag import Tag
from .models.product import Product
from .models.product_tag import ProductTag
from .models.product_image import ProductImage
from .models.product_attribute import ProductAttribute
from .models.product_attribute_value import ProductAttributeValue
from .models.product_variant import ProductVariant
from .models.product_variant_value import ProductVariantValue
from .models.cart import Cart
from .models.order import Order
from .models.order_shipment import OrderShipment
from .models.order_product import OrderProduct
from .models.order_order_product import OrderOrderProduct
from .models.discount import Discount


class CustomAccountAdmin(UserAdmin):
    pass


admin.site.register(Account, CustomAccountAdmin)
admin.site.register(Customer)
admin.site.register(CustomerShipment)
admin.site.register(Collection)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(ProductTag)
admin.site.register(ProductImage)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantValue)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderShipment)
admin.site.register(OrderProduct)
admin.site.register(OrderOrderProduct)
admin.site.register(Discount)
