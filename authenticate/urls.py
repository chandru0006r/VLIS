from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('userlogin/', views.login_user, name='userlogin'),
    path('adminlogin/', views.login_admin, name='adminlogin'),
    path('logout/', views.logout_user, name='logout'),
]
