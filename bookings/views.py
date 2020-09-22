from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BookingDate, BookingTime
from .forms import DateForm, TimeForm

def book_it(booking_time, booking_date, minute):
    """Booking each slot one by one"""
    hours = booking_date.hours
    # get the number of room left
    for k in hours[hour][minute].keys():
        capacity = k
    # update the capacity and book the slot
    new_capacity = capacity - 1
    hours[hour][minute][new_capacity] = hours[hour][minute].pop(capacity)
    hours[hour][minute][new_capacity].append("username")
    booking_time.day = booking_date
    # check if the slot is full
    if new_capacity == 0:
        booking_date.free -= 1

def booking_func(booking_time, booking_date):
    """Booking for the chosen duration"""
    # map the input to index-form to iterate hours list
    indexing = {'08':0, '09':1, '10':2, '11':3, '12':4, '13':5, '14':6,
        '15':7, '16':8, '17':9, '18':10,
        '00':0, '15':1, '30':2, '45':3}
    # index of the hour
    start_h = indexing[booking_time.start_hour]
    end_h = indexing[booking_time.end_hour]

    start_minute = indexing[booking_time.start_minute]
    end_minute = indexing[booking_time.end_minute]
    # initiall value for iterating the minutes
    minute = start_minute
    for hour in range(start_h, end_h+1):
        while True:
            # check if we arrived at the end of the booking duration
            if minute == end_minute:
                if hour == end_h:
                    break
            # not there yet; iterate and book
            if minute == 3:
                # book the slot for this user
                book_it(booking_time, booking_date, minute)
                # next; iterate through the next hour
                minute = 0
                break
            else:
                # book the slot for user
                book_it(booking_time, booking_date, minute)
                # first finish iterating through this hour
                minute += 1


def index(request):
    #return HttpResponse("Welcome to the booking app!")
    if request.method != 'POST':
        # no data submitted; create a blank form.
        day_form = DateForm()
        time_form = TimeForm()
    else:
        # data is submitted.
        day_form = DateForm(data=request.POST)
        time_form = TimeForm(data=request.POST)
        if (day_form.is_valid() and time_form.is_valid()):
            # valid day_form means there's room in this day
            booking_date = day_form.save(commit=False)
            booking_time = time_form.save(commit=False)
            # start booking function
            booking_func(booking_time, booking_day)
            booking_date.save()
            booking_time.save()
            return HttpResponseRedirect(reverse('bookings:index'))

    context = {'day_form':day_form, 'time_form':time_form}
    return render(request, 'bookings/index.html', context)
