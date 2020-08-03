from django.urls import path

from .views import (CategoryCreate, 
    CategoryList, 
    CategoryDetail,
    CategoryUpdate,
    CategoryDelete
)


urlpatterns = [
    path('create/', CategoryCreate.as_view(), name='category-create'),
    path('', CategoryList.as_view(), name='category-list'),
    path('<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='category-update'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='category-delete'),

]