from django.test import TestCase

from ..models import ParkingArea as parking_area_db
from ..models import Ticket as ticket_db
from ..models import Slot as slot_db

from ..modules.base.Parking import Parking
from ..modules.base.Ticket import Ticket
from ..modules.base.Price import Price
from ..modules.base.Slots import Slots

from datetime import datetime
from django.db.models.query import QuerySet


class ParkingClassTestCase(TestCase):

    def setUp(self):
        parking_area = parking_area_db.objects.create(name="test")


        for size in range(4):
            slot_db.objects.create(size=size, parking_area=parking_area)
            slot_db.objects.create(size=size, parking_area=parking_area)

        self.parking = Parking(
            ticket = Ticket(ticket_db),
            price = Price([45, 65, 78, 90], 5),
            slots = Slots(slot_db.objects.filter(parking_area=parking_area) )
        )


    def test_entry(self):
        entry = self.parking.entry(0)

        # this slot will be unavailable(True) in the end of the entry 
        first_slot = slot_db.objects.get(id=1)

        self.assertTrue(isinstance(entry, ticket_db))
        self.assertTrue(entry.slot_size.status)
        self.assertTrue(first_slot.status)



    def test_exit(self):
        slot = slot_db.objects.get(id=1)
        ticket = ticket_db.objects.create(slot_size=slot )
        ticket.slot_size.status = True
        ticket.save()
        token = ticket.token

        exit = self.parking.exit(token)

        self.assertTrue(isinstance(exit, ticket_db))
        self.assertFalse(exit.slot_size.status)
        self.assertEqual(exit.total_price, 0)
        self.assertTrue(isinstance(exit.exit_time, datetime))

    def test_get_slots(self):
        slots = self.parking.get_slots()

        self.assertTrue(isinstance(slots, QuerySet ))
        self.assertEqual(len(slots), 8)



