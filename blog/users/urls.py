from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_users, name='register_users'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'), # type: ignore
]