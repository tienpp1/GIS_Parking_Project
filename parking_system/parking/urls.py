from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('parking/', views.parking_list, name='parking_list'),
    path('parking/<int:pk>/', views.parking_detail, name='parking_detail'),
]
