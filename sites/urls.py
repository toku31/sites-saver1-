from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.sites, name="urls"),
    path('sites/<str:pk>/', views.siteDetail, name="site"),
    path('', views.indexPage, name="index"),
    
    path('create-site', views.createSite, name="create-site"),
    path('update-site/<str:pk>', views.updateSite, name="update-site"),
    path('delete-site/<str:pk>', views.deleteSite, name="delete-site"),
    
    path('sites/category/<str:pk>', views.categorySites, name="category-sites"),
    path('sites/tag/<str:pk>', views.tagSites, name="tag-sites"),
    
    path('create-category', views.createCategory, name="create-category"),
    path('delete-category/<str:pk>', views.deleteCategory, name="delete-category"),
    path('create-tag', views.createTag, name="create-tag"),
    path('delete-tag/<str:pk>', views.deleteTag, name="delete-tag"),
]