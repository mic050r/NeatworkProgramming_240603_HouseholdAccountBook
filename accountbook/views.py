from django.shortcuts import render
from django.views.generic import ListView

from accountbook.models import Category, AccountBook


# Create your views here.

class CategoryListView(ListView):
    model = Category

class AccountbookListView(ListView):
    model = AccountBook