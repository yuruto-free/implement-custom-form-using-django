from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  model = Author
  fields = ['name']
  list_display = ('name',)
  list_filter = ('name',)
  search_fields = ('name',)
  ordering = ('pk',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  model = Book
  fields = ['title', 'author']
  list_display = ('title', 'author')
  list_filter = ('title', 'author')
  search_fields = ('title', 'author')
  ordering = ('pk',)