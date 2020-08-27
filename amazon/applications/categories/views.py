from django.urls import reverse_lazy
from django.views import generic

from .models import Category
from .forms import CategoryForm


class CategoryCreate(generic.CreateView):
    model = Category
    template_name = 'tags/category_create.html'
    form_class = CategoryForm
    
    

class CategoryList(generic.ListView):
    model = Category
    template_name = 'tags/category_list.html'
    context_object_name = 'categories'


class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'tags/category_detail.html'


class CategoryUpdate(generic.UpdateView):
    model = Category
    template_name = 'tags/category_update.html'
    form_class = CategoryForm


class CategoryDelete(generic.DeleteView):
    model = Category
    template_name = 'tags/category_delete.html'
    success_url = reverse_lazy('category-list')
    

        

