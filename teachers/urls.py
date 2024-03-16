from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_teachers, name='teachers'),
    path('<str:category>/', views.get_teachers, name='teachers_by_category')
]
