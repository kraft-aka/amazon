from django.views import generic

from .models import Product


class MainPageView(generic.TemplateView):
    template_name = 'main_page.html'


class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'



