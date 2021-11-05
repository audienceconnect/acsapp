from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('register', views.register, name='dashboard'),
    path('dashboard', views.dashboard, name='login')
]
