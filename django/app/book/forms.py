from django import forms
from django.utils.translation import gettext_lazy as _
from utils.forms import BaseDatalistModelForm
from utils.widgets import Datalist
from . import models

class _BaseFormWithCSS(BaseDatalistModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for field in self.fields.values():
      _classes = field.widget.attrs.get('class', '')
      field.widget.attrs['class'] = f'{_classes} form-control'
      field.widget.attrs['placeholder'] = field.help_text

class AuthorForm(_BaseFormWithCSS):
  class Meta:
    model = models.Author
    fields = ('name',)

class BookForm(_BaseFormWithCSS):
  class Meta:
    model = models.Book
    fields = ('author', 'title')
    widgets = {
      'author': Datalist(attrs={
        'id': 'author-id',
        'use-dataset': True,
        'class': 'form-control',
      }),
    }
    # BaseDatalistModelForm
    datalist_fields = ['author']
    datalist_kwargs = {
      'author': {
        'label': _('Author'),
        'queryset': models.Author.objects.all(),
      },
    }