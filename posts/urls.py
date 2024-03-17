
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('posts/', views.posts_view, name='posts'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
]
