from django import forms
from .widgets import ModelDatalistField
from .models import empty_qs

class BaseDatalistModelForm(forms.ModelForm):
  template_name = 'renderer/utils_form.html'

  class Meta:
    datalist_fields = []
    datalist_kwargs = {}

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #
    # Setup datalist fields
    #
    _meta = getattr(self, 'Meta', None)
    datalist_fields = getattr(_meta, 'datalist_fields', [])
    datalist_kwargs = getattr(_meta, 'datalist_kwargs', {})
    widgets = getattr(_meta, 'widgets', {})
    dynamic_fields = {}
    # Create fields dynamically
    for field_name in datalist_fields:
      widget = widgets.get(field_name, None)
      options = datalist_kwargs.get(field_name, {'queryset': empty_qs})
      dynamic_fields[field_name] = ModelDatalistField(widget=widget, **options)
    # Define extra datalist field
    self._extra_datalist_fields = [field_name for field_name in datalist_fields]
    # Update relevant fields
    self.declared_fields.update(dynamic_fields)
    self.fields.update(self.declared_fields)

  @property
  def datalist_js_template_name(self):
    return 'renderer/utils_datalist_javascript.html'

  @property
  def datalist_ids(self):
    related_fields = [
      self.fields[field_name]
      for field_name in self._extra_datalist_fields if self.fields[field_name].widget.use_dataset()
    ]
    datalist_ids = [field.widget.attrs['id'] for field in related_fields]

    return datalist_ids