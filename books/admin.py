from django.contrib import admin
from .models import Category, Book, BookReview

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookReview)