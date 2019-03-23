from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['reservation_confirmed']




class DateSelected(forms.Form):
    selected_date = forms.DateTimeField(label = 'Date and hour that you want to reserve')
