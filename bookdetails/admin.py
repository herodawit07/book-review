from django.contrib import admin

# Register your models here.
# bookdetails/admin.py
from django.contrib import admin
from .models import Book, Comment

admin.site.register(Book)
admin.site.register(Comment)