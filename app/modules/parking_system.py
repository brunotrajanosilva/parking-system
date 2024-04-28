from ..models import Ticket, Slot
from django.db.models import Q
from django.utils import timezone
from datetime import time, timedelta
from math import ceil
import random

from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet



# car sizes: 3, 2, 1.5, 1
class parking_system:
    #

    def __init__(self):
        self.value = "value"

    def create_ticket(self, CarType):
        find_slot = self.find_slot(CarType)

        if find_slot:
            find_slot.status = True
            find_slot.save()

            ticket = Ticket()

            rand_number = ''

            for i in range(4):
                rand_number += str(random.randint(0,9))

            ticket.number = rand_number
            ticket.car_size = CarType
            ticket.slot = find_slot
            ticket.save()

            return ticket
        
    
    def update_ticket(self, TicketNumber):
        ticket = Ticket.objects.get(number=TicketNumber)
        ticket.exit_time = timezone.now()
        ticket.save()

        return ticket

    def find_slot(self, CarType):

        try:
            slot = Slot.objects.filter(Q(status=False) & Q(size=CarType)).order_by('size')[0]
        
        except IndexError:
            raise Exception('No slots available. Try to choose other size')

        # slot = Slot.objects.filter(Q(status=False) & Q(size__gte=CarType)).order_by('size').first()
        # slot = Slot.objects.first(Q(status=False) & Q(size=CarType))

        
        return slot



    def entry(self, CarType):
        ticket = self.create_ticket(CarType)
        return ticket

    def exit(self, TicketNumber):
        #update ticket
        ticket = self.update_ticket(TicketNumber)

        price = self.calc_price(ticket.slot.size, ticket.entry_time, ticket.exit_time)
        ticket.price = price
        ticket.save()

        # update slot
        slot = Slot.objects.get(id=ticket.slot.id)
        slot.status = False
        slot.save()

        return ticket



    def calc_price(self, slot_size, entry_time, exit_time):
        # prices per each slot size
        prices = (1, 1.5, 2, 3)


        time_parked = exit_time - entry_time
        print(time_parked.total_seconds() / 60)

        interval = timedelta(minutes=30)


        intervals_to_pay = ceil(time_parked / interval)
        # print(intervals_to_pay)

        total_price = intervals_to_pay * prices[slot_size-1]

        return total_price





