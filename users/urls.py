from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    
    path('', views.usersList, name="users-list"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name='account'),
    
    path('edit-account/', views.editAccount, name='edit-account'),
    
    # path('', views.indexPage, name="index"),
    
    # path('create-site', views.createSite, name="create-site"),
    # path('update-site/<str:pk>', views.updateSite, name="update-site"),
    # path('delete-site/<str:pk>', views.deleteSite, name="delete-site"),
]