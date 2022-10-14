from django.forms import ModelForm, widgets
from .models import Review, Site, Category, Tag
from django import forms

class SiteForm(ModelForm):
  class Meta:
      model = Site
      fields = ['title', 'category', 'text', 'link', 'tags']
      # fields = '__all__'
      widgets = {
        'tags': forms.CheckboxSelectMultiple
      }
      
  def __init__(self, *args, **kwargs):
    super(SiteForm, self).__init__(*args, **kwargs)
    
    self.fields['title'].widget.attrs.update(
      { 'class': 'form-input', 'placeholder': 'タイトルを入力'})
    
    self.fields['text'].widget.attrs.update(
      { 'class': 'form-input'})
    
    self.fields['link'].widget.attrs.update(
      { 'class': 'form-input'})
      
    # for name, field in self.fields.items():
    #   field.widget.attrs.update({'class': 'form-input'})
    

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['value', 'body']
    
    labels = {
      'value':'評価してください',
      'body': 'コメントお願いします'
    }

  def __init__(self, *args, **kwargs):
    super(ReviewForm, self).__init__(*args, **kwargs)
    
    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-input'})
      
      
class CategoryForm(ModelForm):
  class Meta:
      model = Category
      fields = ['name']
      
  def __init__(self, *args, **kwargs):
    super(CategoryForm, self).__init__(*args, **kwargs)
    
    self.fields['name'].widget.attrs.update(
      { 'class': 'form-input'})



class TagForm(ModelForm):
  class Meta:
      model = Tag
      fields = ['name']
      
  def __init__(self, *args, **kwargs):
    super(TagForm, self).__init__(*args, **kwargs)
    
    self.fields['name'].widget.attrs.update(
      { 'class': 'form-input'})
