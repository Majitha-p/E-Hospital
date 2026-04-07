from django import forms

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_data': DateInput(),
            
        }
        
        labels ={
            'p_name' : "Patient Name: ",
            'p_phone' : "Phone Number: ",
            'p_email' : "E-mail",
            'doc_name' : "Doctor Name",
            'booking_data' : "Booking Date",
        }