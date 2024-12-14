from django.shortcuts import render
from .models import Guest, Reservation

def list_guests(request):
    guests = Guest.objects.all()
    return render(request, 'list_guests.html', {'guests': guests})

def list_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'list_reservations.html', {'reservations': reservations})
