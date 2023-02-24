from django.urls import path
from .views import CategoryListView, \
    ProductListView, ProductDetailView, \
    CategoryProductListView, \
    ProductCreateView, \
    ProductDeleteView, \
    ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('categories/<slug:slug>/', CategoryProductListView.as_view(), name='category_product_list'),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
