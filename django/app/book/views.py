from django.views.generic import (
  ListView,
  CreateView,
  UpdateView,
  DeleteView,
)
from django.urls import reverse_lazy, reverse
from . import models, forms

# ==========
# For Author
# ==========
class ListAuthor(ListView):
  model = models.Author
  template_name = 'book/author_list.html'
  paginate_by = 10
  context_object_name = 'authors'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['create_path'] = reverse('book:create_author')

    return context

class _CommonAuthorView:
  model = models.Author
  form_class = forms.AuthorForm
  template_name = 'book/author_form.html'
  success_url = reverse_lazy('book:list_author')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['parent_path'] = self.success_url

    return context

class CreateAuthor(_CommonAuthorView, CreateView):
  pass

class UpdateAuthor(_CommonAuthorView, UpdateView):
  pass

class DeleteAuthor(DeleteView):
  raise_exception = True
  http_method_names = ['post']
  model = models.Author
  success_url = reverse_lazy('book:list_author')

# ========
# For Book
# ========
class ListBook(ListView):
  model = models.Book
  template_name = 'book/book_list.html'
  paginate_by = 10
  context_object_name = 'books'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['create_path'] = reverse('book:create_book')

    return context

class _CommonBookView:
  model = models.Book
  form_class = forms.BookForm
  template_name = 'book/book_form.html'
  success_url = reverse_lazy('book:list_book')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['parent_path'] = self.success_url

    return context

class CreateBook(_CommonBookView, CreateView):
  pass

class UpdateBook(_CommonBookView, UpdateView):
  pass

class DeleteBook(DeleteView):
  raise_exception = True
  http_method_names = ['post']
  model = models.Book
  success_url = reverse_lazy('book:list_book')