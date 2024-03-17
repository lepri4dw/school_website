from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('thanks/', views.thanks_view, name='thanks')
]
