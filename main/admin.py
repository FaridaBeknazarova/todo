from django.contrib import admin

# Register your models here.

from .models import ToDo, Book

admin.site.register(ToDo)

admin.site.register(Book)