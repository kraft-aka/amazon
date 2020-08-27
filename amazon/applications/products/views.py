from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Product, ProductItem
from .forms import ProductForm, ProductItemForm


class MainPageView(generic.TemplateView):
    template_name = 'main_page.html'


class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products_list.html'

    def get_queryset(self):
        qs = Product.objects.all()
        search = self.request.GET.get('q')
        if search:
            qs = Product.objects.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
        return qs


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'products/product_create.html'
    context_object_name = 'product-create'
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user.profile
        form.save()
        return HttpResponseRedirect(product.get_absolute_url())


class ProductUpdateView(generic.UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm
    

class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products-list')
    

class ProductItemCreateView(generic.CreateView):
    model = ProductItem
    template_name = 'products/product_item_create.html'
    context_object_name = 'product-item'
    form_class = ProductItemForm
    success_url = reverse_lazy('products-list')


class ProductItemDetailView(generic.DetailView):
    model = ProductItem
    context_object_name = 'item'
    template_name = 'products/product_item_detail.html'
    

class ProductItemDeleteView(generic.DeleteView):
    model = ProductItem
    template_name = 'products/product_item_delete.html'
    success_url = reverse_lazy('products-list')


