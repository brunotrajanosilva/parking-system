from django.test import TestCase
from ..models import ParkingArea, Slot, Ticket
from datetime import datetime 

import uuid
#  test models


class ModelsTestCase(TestCase):
    def setUp(self):
        pass

    def test_parking_area(self):
        name = 'test area'
        parking = ParkingArea.objects.create(name=name)

        self.assertEqual(parking.name, name)

    
    def test_slot(self):
        name = 'parking for slot'
        parking = ParkingArea.objects.create(name=name)
        slot = Slot.objects.create(parking_area=parking, size=0)

        self.assertFalse(slot.status)
        self.assertEqual(slot.parking_area.name, name)


    def test_ticket(self):
        name = 'parking for slot'
        parking = ParkingArea.objects.create(name=name)
        slot = Slot.objects.create(parking_area=parking, size=0)
        ticket = Ticket.objects.create(slot_size=slot, exit_time=datetime.now())
        ticket.total_price = 2600.34
        ticket.save()

        self.assertTrue(uuid.UUID(str(ticket.token)) )
        self.assertTrue(isinstance(ticket.total_price, float))
