from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from accountbook.models import Category, AccountBook


# Create your views here.

class CategoryListView(ListView):
    model = Category

class AccountbookListView(ListView):
    model = AccountBook

class AccountBookCreateView(CreateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('accountbook:accountbook_list')

class AccountBookUpdateView(UpdateView):
    model = AccountBook
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('accountbook:accountbook_list')

class AccountBookDeleteView(DeleteView):
    model = AccountBook
    success_url = reverse_lazy('accountbook:accountbook_list')

