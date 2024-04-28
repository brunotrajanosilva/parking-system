from django.db import models


# Create your models here.

car_choices = (
    (1, 'SM'),
    (2, 'MD'),
    (3, 'LG'),
    (4, 'XL'),
)

class Slot(models.Model):
    size = models.IntegerField(choices=car_choices)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'id:{self.id}, size:{ self.size}, status: {self.status}'

class Ticket(models.Model):
    number = models.CharField(max_length=4)
    car_size = models.IntegerField(choices=car_choices)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f'number:{self.number}, car_size:{self.car_size}, entry_time:{self.entry_time}, exit_time:{self.exit_time}'

