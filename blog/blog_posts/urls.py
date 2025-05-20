from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('new_post/', views.new_post, name='new_post'),
    path('posts/<int:post_id>/',views.single_post_page, name='single_post_page'),
]