from django.shortcuts import render, get_object_or_404
from .models import ParkingLot

# 1. Trang chủ
def home(request):
    return render(request, 'parking/home.html')

# 2. Danh sách các bãi đỗ xe
def parking_list(request):
    # Lấy tất cả danh sách bãi đỗ xe từ database
    parking_lots = ParkingLot.objects.all()
    return render(request, 'parking/parking_list.html', {
        'parking_lots': parking_lots
    })

# 3. Chi tiết một bãi đỗ xe cụ thể
def parking_detail(request, pk):
    # Trả về lỗi 404 nếu không tìm thấy ID bãi xe
    parking_lot = get_object_or_404(ParkingLot, pk=pk)
    return render(request, 'parking/parking_detail.html', {
        'parking_lot': parking_lot
    })

# 4. Bản đồ GIS hiển thị các bãi đỗ xe
def map_view(request):
    parking_lots = ParkingLot.objects.values(
        'name', 'address', 'latitude', 'longitude'
    )
    return render(request, 'parking/map.html', {
        'parking_lots': list(parking_lots)
    })
