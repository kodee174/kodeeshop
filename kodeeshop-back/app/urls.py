from django.urls import re_path
from .views import CustomerListView, CustomerDetailView, CollectionListView, CollectionDetailView, \
    TagListView, TagDetailView, ProductListView, ProductDetailView

urlpatterns = [
    re_path(r'^customers$', CustomerListView.as_view()),
    re_path(r'^customers/(?P<id_customer>\d+)$', CustomerDetailView.as_view()),
    re_path(r'^collections$', CollectionListView.as_view()),
    re_path(r'^collections/(?P<id_collection>\d+)$', CollectionDetailView.as_view()),
    re_path(r'^tags$', TagListView.as_view()),
    re_path(r'^tags/(?P<id_tag>\d+)$', TagDetailView.as_view()),
    re_path(r'^products$', ProductListView.as_view()),
    re_path(r'^products/(?P<id_product>\d+)$', ProductDetailView.as_view()),
]
