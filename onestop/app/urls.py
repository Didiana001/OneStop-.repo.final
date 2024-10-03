from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]