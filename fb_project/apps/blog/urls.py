from django.urls import path

from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('category/list',CategoryListView.as_view(),name = 'category_list'),
    path('post/list/<slug:category_slug>/',PostListView.as_view(),name='post_category_list'),
    path('post/list/',PostListView.as_view(), name = 'post_list'),
    path('post/detail/<int:pk>/',PostDetailView.as_view(),name = 'post_detail'),
    path('user/profile/<int:pk>/',ProfileView.as_view(),name = 'profile')
]