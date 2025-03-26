from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Laptop

class LaptopList(ListView):
    model = Laptop
    template_name = 'laptop_list.html'
    context_object_name = 'laptops'

class LaptopDetail(DetailView):
    model = Laptop
    template_name = 'laptop_detail.html'
    context_object_name = 'laptop'

class LaptopCreate(CreateView):
    model = Laptop
    template_name = 'laptop_form.html'
    fields = ['brand', 'model', 'price', 'processor', 'ram', 'storage', 'display', 'graphics']
    success_url = reverse_lazy('laptop_list')

class LaptopUpdate(UpdateView):
    model = Laptop
    template_name = 'laptop_form.html'
    fields = ['brand', 'model', 'price', 'processor', 'ram', 'storage', 'display', 'graphics']
    success_url = reverse_lazy('laptop_list')

class LaptopDelete(DeleteView):
    model = Laptop
    template_name = 'laptop_confirm_delete.html'
    success_url = reverse_lazy('laptop_list')