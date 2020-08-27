
from django.urls import path, include

from .import views


urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products-list'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('item/create/', views.ProductItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/', views.ProductItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/delete/', views.ProductItemDeleteView.as_view(), name='item-delete'),
]
