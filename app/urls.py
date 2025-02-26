from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup',views.register,name='signup'),
    path('log',views.log,name='log'),
    path('energy_cost',views.energy_cost1,name='energy_cost'),
    path('emmission_pathways',views.emmission_pathways,name='emmission_pathways'),
    path('economic_forecast',views.economic_forecast1,name='economic_forecast'),
]