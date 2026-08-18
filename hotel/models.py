from django.db import models

# Create your models here.


room_numbers = [
    ('101', '101'),
    ('102', '102'),
    ('103', '103'),
    ('104', '104'),
    ('201', '201'),
    ('202', '202'),
    ('203', '203'),
    ('204', '204'),
]
class Guests(models.Model):


    name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    p_address = models.TextField()
    aadhar_ID = models.CharField(unique = True, max_length=12)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=3, unique=True, choices=room_numbers)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    guest = models.ForeignKey(Guests, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    
    def __str__(self):
        return str(self.room_number)

