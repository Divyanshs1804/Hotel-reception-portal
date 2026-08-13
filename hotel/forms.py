from django.forms import ModelForm
from .models import Guests, Booking, Room
from django.contrib.auth.models import User
class GuestsForm(ModelForm):
    class Meta:
        model = Guests
        fields = "__all__"


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
