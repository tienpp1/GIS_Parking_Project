from django.urls import path
from . import views
from .views import map_view

urlpatterns = [
    # Trang chủ
    path('', views.home, name='home'),
    
    # Danh sách bãi đỗ xe
    path('parking/', views.parking_list, name='parking_list'),
    
    # Chi tiết từng bãi đỗ xe (truyền tham số ID là số nguyên)
    path('parking/<int:pk>/', views.parking_detail, name='parking_detail'),
    
    # Bản đồ GIS bãi đỗ xe
    path('map/', views.map_view, name='map_view'),
    path('<int:pk>/', views.parking_detail, name='parking_detail'),

]