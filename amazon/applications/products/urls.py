
from django.urls import path, include

from .import views


urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]
