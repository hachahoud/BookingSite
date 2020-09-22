from django.db import models
from django.utils import timezone
from users.models import CustomUser

CAPACITY = 25
class BookingDate(models.Model):
    """Managing the booking date"""
    date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    # 8 available/working-hours initially for each day
    free = 8
    # the maximum capacity of the room
    capacity = 25
    # each hour-list contains a list of 4 elements
    # each element contains a dict representing a part of the hour
    # a dict has as key:the capacity, and value is a list of users who booked it

    hours = [
        [{CAPACITY:[]}, {CAPACITY:[]}, {CAPACITY:[]}, {CAPACITY:[]}]
        for _ in range(8)]


class BookingTime(models.Model):
    """Managing the booking timing for a specific day"""
    # hours
    EIGHT = '08'
    NINE = '09'
    TEN = '10'
    ELEVEN = '11'
    TWELVE = '12'
    ONE = '13'
    TWO = '14'
    THREE = '15'
    FOUR = '16'
    FIVE = '17'
    SIX = '18'
    # minutes; 15 minutes apart
    OCLOCK = '00'
    QUARTER_PAST = '15'
    Half_PAST = '30'
    QUARTER_TO = '45'

    START_HOUR_CHOICES = [
        (EIGHT, '08'),
        (NINE, NINE),
        (TEN, TEN),
        (ELEVEN, ELEVEN),
        (TWELVE, TWELVE),
        (ONE, ONE),
        (TWO,TWO),
        (THREE, THREE),
        (FOUR, FOUR),
        (FIVE, FIVE),
    ]
    END_HOUR_CHOICES = START_HOUR_CHOICES + [(SIX, SIX)]

    MINUTES_CHOICES = [
        (OCLOCK, '00'),
        (QUARTER_PAST, '15'),
        (Half_PAST, '30'),
        (QUARTER_TO, '45'),
    ]

    day = models.ForeignKey(BookingDate, on_delete=models.CASCADE)

    start_hour = models.CharField(max_length=2, choices=START_HOUR_CHOICES, default=EIGHT)
    start_minute = models.CharField(max_length=2, choices=MINUTES_CHOICES, default=OCLOCK)

    end_hour = models.CharField(max_length=2, choices=END_HOUR_CHOICES, default=SIX)
    end_minute = models.CharField(max_length=2, choices=MINUTES_CHOICES, default=OCLOCK)
    

