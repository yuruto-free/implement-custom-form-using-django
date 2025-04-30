from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'book'

urlpatterns = [
  path('', RedirectView.as_view(pattern_name='index')),
  # Author
  path('list/authors', views.ListAuthor.as_view(), name='list_author'),
  path('create/author', views.CreateAuthor.as_view(), name='create_author'),
  path('update/author/<int:pk>', views.UpdateAuthor.as_view(), name='update_author'),
  path('delete/author/<int:pk>', views.DeleteAuthor.as_view(), name='delete_author'),
  # Book
  path('list/books', views.ListBook.as_view(), name='list_book'),
  path('create/book', views.CreateBook.as_view(), name='create_book'),
  path('update/book/<int:pk>', views.UpdateBook.as_view(), name='update_book'),
  path('delete/book/<int:pk>', views.DeleteBook.as_view(), name='delete_book'),
]