from django.contrib import admin
from .models import Area, ParkingType, ParkingLot, Price

# 1. Đăng ký các model đơn giản (chỉ hiển thị mặc định)
admin.site.register(Area)
admin.site.register(ParkingType)
admin.site.register(Price)

# 2. Đăng ký ParkingLot với cấu hình chi tiết (Advanced)
@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    # Các cột hiển thị ngoài danh sách
    list_display = ('name', 'area', 'parking_type', 'status', 'available_slots', 'capacity')
    
    # Bộ lọc bên phải màn hình
    list_filter = ('area', 'status', 'parking_type')
    
    # Ô tìm kiếm (theo tên bãi xe)
    search_fields = ('name',)
    
    # Cho phép sửa nhanh trạng thái ngay tại danh sách mà không cần bấm vào chi tiết
    list_editable = ('status',)
    
    # Phân trang (hiển thị 20 dòng mỗi trang)
    list_per_page = 20