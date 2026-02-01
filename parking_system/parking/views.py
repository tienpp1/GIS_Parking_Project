from django.shortcuts import render, get_object_or_404
from .models import ParkingLot


def parking_list(request):
    parking_lots = ParkingLot.objects.all()
    return render(request, 'parking/parking_list.html', {
        'parking_lots': parking_lots
    })


def parking_detail(request, pk):
    parking_lot = get_object_or_404(ParkingLot, pk=pk)
    return render(request, 'parking/parking_detail.html', {
        'parking_lot': parking_lot
    })
def home(request):
    return render(request, 'parking/home.html')
