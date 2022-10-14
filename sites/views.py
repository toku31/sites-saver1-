from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Site, Category, Tag
from .forms import SiteForm, ReviewForm, CategoryForm, TagForm
from django.db.models import Q 
from django.core.exceptions import ValidationError

# def categoryList(request):
#     categories = Category.objects.all()
#     print('categories', categories)
#     context = {'categories': categories}
#     return render(request, 'urls/urls-list.html', context)
      
# class CategoryPostView(ListView):
#     model = Post
#     template_name = 'blog/category_post.html'

#     def get_queryset(self):
#         category_slug = self.kwargs['category_slug']
#         self.category = get_object_or_404(Category, slug=category_slug)
#         qs = super().get_queryset().filter(category=self.category)
#         return qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = self.category
#         return context

# def sites(request):
#   sites = Site.objects.all()
#   categories = Category.objects.all()
#   tags = Tag.objects.all()
#   # print('categories', categories)
#   # print('tags', tags)
#   context = {'sites': sites, 'categories':categories, 'tags':tags}
#   return render(request, 'urls/urls-list.html', context)

def sites(request):
  search_query = ''
  categories = Category.objects.all()
  tags = Tag.objects.all()
  # print('categories', categories)
  # print('tags', tags)
  if request.GET.get('search_query'):
    search_query=request.GET.get('search_query')
  # print('SEARCH: ', search_query)
  # sites = Site.objects.all()
  sites = Site.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
  print('sites', sites)
  
  page = request.GET.get('page')
  results = 10
  paginator = Paginator(sites, results)
  
  try:
    sites = paginator.page(page)
  except PageNotAnInteger:
    page = 1
    sites = paginator.page(page)
  except EmptyPage:
    page = paginator.num_pages
    sites = paginator.page(page)
    
  custom_range = range(1, 1000)
  
  print('page', page)
  context = {'sites': sites, 'categories':categories, 'search_query':search_query, 'tags':tags, 'paginator':paginator, 'custom_range': custom_range}
  return render(request, 'urls/urls-list.html', context)


# def usersList(request):
#   search_query = ''
  
#   if request.GET.get('search_query'):
#     search_query=request.GET.get('search_query')
  
#   print('SEARCH: ', search_query)
    
#   # profiles = Profile.objects.all()
#   profiles = Profile.objects.filter(Q(name__icontains=search_query) | Q(short_intro__icontains=search_query))
#   context = {'profiles': profiles, 'search_query': search_query}
#   return render(request, 'users/users.html', context)


def siteDetail(request, pk):
  try:
    print('pk', pk)
    siteObj = Site.objects.get(id=pk)
    # siteObj = get_object_or_404(Site, id=pk)
  except ValidationError:
    raise Http404
  except siteObj.DoesNotExist:
    raise Http404
  tags = siteObj.tags.all()
  print('siteObj:', siteObj)
  form = ReviewForm()
  
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    review = form.save(commit=False)
    review.site = siteObj
    review.owner = request.user.profile
    review.save()
    
    siteObj.getVoteCount
    
    messages.success(request, 'あなたのフィードバックを受け付けました')
    
  return render(request, 'urls/site-details.html', {'site': siteObj, 'tags': tags, 'form': form})


def indexPage(request):
  return render(request, 'index.html')

@login_required(login_url="login")
def createSite(request):
  profile = request.user.profile
  form = SiteForm()
  if request.method == 'POST':
    # newtags = request.POST.get('newtags').replace(',',  " ").split()
    print(request.POST)
    form = SiteForm(request.POST)
    if form.is_valid():
      # form.save()
      site = form.save(commit=False)
      site.user= profile
      site.save()
      form.save_m2m()
      # for tag in newtags:
      #           tag, created = Tag.objects.get_or_create(name=tag)
      #           site.tags.add(tag)
      return redirect('urls')
    
    # if form.is_valid():
    #   form.save()
    #   return redirect('urls')
    
  context = {'form': form}
  return render(request, "urls/site_form.html", context)


@login_required(login_url="login")
def createCategory(request):
  categories = Category.objects.all()
  form = CategoryForm()
   
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    # print(request.POST)
    if form.is_valid():
      form.save()
      return redirect('urls')
      
  context = {'form': form, 'categories': categories}
  return render(request, "urls/category_form.html", context)


@login_required(login_url="login")
def deleteCategory(request, pk):
  category = Category.objects.get(id=pk)
  if request.method=='POST':
    category.delete()
    return redirect('urls')
  context = {'object': category}
  return render(request, 'urls/delete_template.html', context)


@login_required(login_url="login")
def createTag(request):
  tags = Tag.objects.all()
  form = TagForm()
  
  if request.method == 'POST':
    form = TagForm(request.POST)
    # print(request.POST)
    if form.is_valid():
      form.save()
      return redirect('urls')
    
  context = {'form': form, 'tags': tags}
  return render(request, "urls/tag_form.html", context)


@login_required(login_url="login")
def deleteTag(request, pk):
  tag = Tag.objects.get(id=pk)
  if request.method=='POST':
    tag.delete()
    return redirect('urls')
  context = {'object': tag}
  return render(request, 'urls/delete_template.html', context)


@login_required(login_url="login")
def updateSite(request, pk):
  site = Site.objects.get(id=pk)
  form = SiteForm(instance=site)
  
  if request.method == 'POST':
    # print(request.POST)
    form = SiteForm(request.POST, instance=site)
    if form.is_valid():
      form.save()
      return redirect('urls')
    
  context = {'form': form}
  return render(request, "urls/site_form.html", context)


@login_required(login_url="login")
def deleteSite(request, pk):
  site = Site.objects.get(id=pk)
  if request.method=='POST':
    site.delete()
    return redirect('urls')
  context = {'object': site}
  return render(request, 'urls/delete_template.html', context)


def categorySites(request, pk):
  category = Category.objects.get(id=pk)
  # print('category', category)
  cate_sites = category.site_set.all()
  # print('cate_sites', cate_sites)
  tags = Tag.objects.all()
  # print('tags', tags)
  categories = Category.objects.all()
  context = {'cate_sites': cate_sites, 'tags': tags, 'categories':categories, 'category':category}
  return render(request, 'urls/category_sites.html', context)


def tagSites(request, pk):
  tag = Tag.objects.get(id=pk)
  # print('category', tag)
  tag_sites = tag.site_set.all()
  # print('cate_sites', tag_sites)
  tags = Tag.objects.all()
  # print('tags', tags)
  categories = Category.objects.all()
  context = {'tag_sites': tag_sites, 'tags': tags, 'categories':categories, 'tag':tag}
  return render(request, 'urls/tag_sites.html', context)


# def categoryList(request):
#   tags = Tag.objects.all()
#   print('tags', tags)
#   categories = Category.objects.all()
#   print('categories', categories)
#   context = {'tags': tags, 'categories':categories}
#   return render(request, 'urls/category-list.html', context)