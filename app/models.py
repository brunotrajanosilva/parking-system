from django.db import models
import uuid



car_choices = (
    (0, 'SM'),
    (1, 'MD'),
    (2, 'LG'),
    (3, 'XL'),
)

class ParkingArea(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Slot(models.Model):
    size = models.IntegerField(choices=car_choices)
    status = models.BooleanField(default=False)
    parking_area = models.ForeignKey(ParkingArea, on_delete=models.CASCADE, related_name='slots')


    def __str__(self):
        return f'id:{self.id}, size:{ self.size}, status: {self.status}'

class Ticket(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slot_size = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='slots')
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    total_price= models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f'token:{self.token}, slot_size:{self.slot_size}, entry_time:{self.entry_time}, exit_time:{self.exit_time}, total:{self.total_price}'

