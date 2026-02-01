# 🚗 Hệ thống quản lý bãi đỗ xe tích hợp GIS

## 📌 Giới thiệu
Đây là đồ án môn GIS xây dựng hệ thống quản lý và hiển thị bãi đỗ xe trên nền tảng Web, 
kết hợp Django và bản đồ GIS nhằm hỗ trợ quản lý và người dùng tra cứu bãi đỗ xe thuận tiện.

## 🛠 Công nghệ sử dụng
- Python + Django
- SQLite
- Leaflet (GIS)
- HTML, CSS, JavaScript
- Chart.js (thống kê)

## 🔑 Chức năng chính

### I. Chức năng quản lý (Django Admin)
- Quản lý bãi đỗ xe (thêm / sửa / xóa)
- Quản lý khu vực hành chính (quận / huyện)
- Quản lý loại bãi đỗ xe (xe máy, ô tô, hỗn hợp)
- Quản lý giá vé theo loại bãi và khung giờ
- Quản lý người dùng (Admin, quản lý, người dùng)

### II. Chức năng hiển thị Web
- Trang danh sách bãi đỗ xe
- Trang chi tiết bãi đỗ xe
- Trang bản đồ GIS hiển thị các bãi đỗ xe
- Tìm kiếm & lọc bãi đỗ xe theo khu vực, loại bãi, trạng thái

### III. Chức năng GIS
- Hiển thị bãi đỗ xe trên bản đồ Leaflet
- Marker phân loại theo trạng thái:
  - 🟢 Còn chỗ
  - 🟡 Gần đầy
  - 🔴 Hết chỗ
- Click marker để xem thông tin chi tiết

### IV. Thống kê
- Thống kê doanh thu theo tháng
- Hiển thị bảng và biểu đồ đơn giản

## 🚀 Hướng dẫn chạy project

```bash
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Truy cập: http://127.0.0.1:8000
