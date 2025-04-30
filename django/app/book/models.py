from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
  name = models.CharField(
    max_length=64,
    verbose_name=_('Name'),
    help_text=_('Max length of this field is 64.'),
  )

  def get_header(self):
    return [_('Name')]

  def get_members(self):
    return [self.name]

  def get_update_url(self):
    return reverse('book:update_author', kwargs={'pk': self.pk})

  def get_delete_url(self):
    return reverse('book:delete_author', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name

class Book(models.Model):
  author = models.ForeignKey(
    Author,
    verbose_name=_('Author'),
    on_delete=models.CASCADE,
    related_name='books',
  )
  title = models.CharField(
    max_length=255,
    verbose_name=_('Title'),
    help_text=_('Max length of this field is 255.'),
  )

  def get_header(self):
    return [_('Author'), _('Title')]

  def get_members(self):
    return [self.author.name, self.title]

  def get_update_url(self):
    return reverse('book:update_book', kwargs={'pk': self.pk})

  def get_delete_url(self):
    return reverse('book:delete_book', kwargs={'pk': self.pk})

  def __str__(self):
    return f'{self.title}({self.author})'