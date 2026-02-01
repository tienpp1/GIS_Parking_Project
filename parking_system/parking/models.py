from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên khu vực")

    class Meta:
        verbose_name = "Khu vực"
        verbose_name_plural = "Khu vực"

    def __str__(self):
        return self.name



class ParkingType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Loại bãi đỗ")

    class Meta:
        verbose_name = "Loại bãi đỗ xe"
        verbose_name_plural = "Loại bãi đỗ xe"

    def __str__(self):
        return self.name



class ParkingLot(models.Model):
    STATUS_CHOICES = [
        ('open', 'Đang hoạt động'),
        ('closed', 'Tạm ngưng'),
    ]

    name = models.CharField(max_length=100, verbose_name="Tên bãi đỗ xe")
    address = models.CharField(max_length=200, verbose_name="Địa chỉ")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Vĩ độ")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Kinh độ")

    capacity = models.IntegerField(verbose_name="Tổng số chỗ")
    available_slots = models.IntegerField(verbose_name="Số chỗ trống")

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='open',
        verbose_name="Trạng thái"
    )

    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Khu vực"
    )

    parking_type = models.ForeignKey(
        ParkingType,
        on_delete=models.CASCADE,
        verbose_name="Loại bãi"
    )

    class Meta:
        verbose_name = "Bãi đỗ xe"
        verbose_name_plural = "Bãi đỗ xe"

    def __str__(self):
        return self.name



class Price(models.Model):
    parking_type = models.ForeignKey(
        ParkingType,
        on_delete=models.CASCADE,
        verbose_name="Loại bãi"
    )
    price_per_hour = models.FloatField(verbose_name="Giá theo giờ")
    time_range = models.CharField(max_length=50, verbose_name="Khung giờ")

    class Meta:
        verbose_name = "Giá vé"
        verbose_name_plural = "Giá vé"

    def __str__(self):
        return f"{self.parking_type} - {self.price_per_hour}"



class Revenue(models.Model):
    parking_lot = models.ForeignKey(
        ParkingLot,
        on_delete=models.CASCADE,
        verbose_name="Bãi đỗ xe"
    )
    month = models.IntegerField(verbose_name="Tháng")
    year = models.IntegerField(verbose_name="Năm")
    total_amount = models.FloatField(verbose_name="Tổng doanh thu")

    class Meta:
        verbose_name = "Doanh thu"
        verbose_name_plural = "Doanh thu"



class ActivityLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Người thực hiện"
    )
    parking_lot = models.ForeignKey(
        ParkingLot,
        on_delete=models.CASCADE,
        verbose_name="Bãi đỗ xe"
    )
    action = models.CharField(max_length=200, verbose_name="Hành động")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Thời gian"
    )

    class Meta:
        verbose_name = "Lịch sử hoạt động"
        verbose_name_plural = "Lịch sử hoạt động"

