from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q 
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm

def loginUser(request):
  # print('ログインページ１')
  page = 'login'
  
  # すでにログインしている人にはログインページを見せない
  if request.user.is_authenticated:
    return redirect('urls')
    
  if request.method == 'POST':
    # print('ログインページ２')
    # print(request.POST)
    # print("request.data", request.data) エラー
    username = request.POST['username']
    password = request.POST['password']
    
    try: 
      user = User.objects.get(username=username)
    except:
      # messages.error(request, 'Username does not exist')
      messages.error(request, 'ユーザ名が存在しません')
      return redirect('login')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        messages.success(request, 'ログインしました')
        # messages.success(request, 'You are now logged in')
        return redirect('urls')
    else:
        # messages.error(request, 'Invalid credentials')
        messages.error(request, 'ユーザ名またはパスワードが不正です')
        # print('Username Or Password is incorrect')
        return redirect('edit-account')
    
  return render(request, 'users/login_register.html')

def logoutUser(request):
  logout(request)
  messages.info(request, 'ログアウトしました')
  print('ログアウトしました')
  return redirect('login')


def registerUser(request):
  page = 'register'
  form = CustomUserCreationForm()
    
  if request.method == 'POST':
    # print('ログインページ２')
    # print(request.POST)
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user=form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      messages.success(request, 'ユーザアカウントを作成しました!')
      
      # 登録後　ログインする
      login(request, user)
      return redirect('edit-account')
    else:
      messages.error(request, '登録中にエラーが発生しました')
      
  context = {'page': page, 'form':form}
  return render(request, 'users/login_register.html', context)


def usersList(request):
  search_query = ''
  
  if request.GET.get('search_query'):
    search_query=request.GET.get('search_query')
  
  print('SEARCH: ', search_query)
    
  # profiles = Profile.objects.all()
  profiles = Profile.objects.filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query))
  context = {'profiles': profiles, 'search_query': search_query}
  return render(request, 'users/users.html', context)


def userProfile(request, pk):
  profile = Profile.objects.get(id=pk)
  context = {'profile': profile}
  print('profile:', profile.profile_image)
  return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
  profile = request.user.profile
  context = {'profile': profile}
  return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
  profile = request.user.profile
  form = ProfileForm(instance=profile)
  if request.method=='POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      form.save()
      return redirect('account')
    
    
  context={'form': form}
  return render(request, 'users/profile_form.html', context)