from django import forms
from django.core.exceptions import ValidationError
from .models import BookingDate, BookingTime

class DateForm(forms.ModelForm):
    class Meta:
        model = BookingDate
        fields = ['date']

    def clean_date(self):
        # the date input from the user
        data = self.cleaned_data['date']
        # check if the date is already booked fully
        date = BookingDate.objects.filter(date=data)
        if date:
            if date.free==0:
                raise ValidationError("There's no room left for this day to book!")
        
        return data
    

class TimeForm(forms.ModelForm):
    
    class Meta:
        model = BookingTime
        fields = ['start_hour', 'start_minute', 'end_hour', 'end_minute']

    