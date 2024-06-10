from django.contrib import admin

from accountbook.models import AccountBook, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(AccountBook)