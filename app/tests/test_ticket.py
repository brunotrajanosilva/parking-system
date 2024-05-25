from django.test import TestCase
from ..models import Ticket as ticket_DB
from ..models import Slot as slot_DB
from ..models import ParkingArea as parking_area_DB

from ..modules.base.Ticket import Ticket


from datetime import datetime, timedelta


class TicketClassTestCase(TestCase):

    def setUp(self):
        self.Ticket = Ticket(ticket_DB)

        parking_test = parking_area_DB.objects.create(name='parking_area_test')
        self.slot_size = slot_DB.objects.create(size=2, parking_area=parking_test)



    def test_create_ticket(self):
        create = self.Ticket.create_ticket(self.slot_size)

        self.assertTrue(isinstance(create, ticket_DB))
        self.assertTrue(isinstance(create.entry_time, datetime))
        self.assertIsNone(create.exit_time)
        self.assertIsNone(create.total_price)


    def test_end_ticket(self):
        new_ticket = ticket_DB.objects.create(slot_size=self.slot_size)
        token = new_ticket.token

        end_ticket = self.Ticket.end_ticket(token)

        self.assertTrue(isinstance(end_ticket, ticket_DB))
        self.assertTrue(isinstance(end_ticket.entry_time, datetime))
        self.assertTrue(isinstance(end_ticket.exit_time, datetime))
        self.assertIsNone(end_ticket.total_price)


