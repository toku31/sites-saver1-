from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields =['first_name', 'email', 'username', 'password1', 'password2']
    labels = {
      'first_name': '名前',
      'email': 'メールアドレス',
      'username': 'ユーザネーム',
      # 'password1': 'パスワード',
      # 'password2': 'パスワード(確認)',
    }
    
  def __init__(self, *args, **kwargs):
    super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    
    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-input'})
    
    # self.fields['title'].widget.attrs.update(
    #   { 'class': 'form-input', 'placeholder': 'タイトルを入力'})
    
    # self.fields['text'].widget.attrs.update(
    #   { 'class': 'form-input'})


class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['name', 'email', 'username', 'location',
              'short_intro','bio', 'profile_image', 'social_github',
              'social_website']
    # fields = '__all__'
    
  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    
    for name, field in self.fields.items():
      field.widget.attrs.update({'class': 'form-input'})