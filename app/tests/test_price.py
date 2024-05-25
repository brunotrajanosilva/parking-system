from django.test import TestCase
from ..models import Slot as slot_db
from ..models import Ticket as ticket_db
from ..models import ParkingArea as parking_db

from ..modules.base.Price import Price

from datetime import datetime, timedelta


class PriceClassTestCase(TestCase):

    def setUp(self):
        self.Price = Price([12, 23, 33, 60], 10)


    def test_price_by_size(self):
        size0 = self.Price.get_price_by_size(0)
        size1 = self.Price.get_price_by_size(1)

        self.assertEqual(size0, 12)
        self.assertEqual(size1, 23)


    def test_minutes_parked(self):
        entry = datetime.now()

        minutes = timedelta(minutes=37, seconds=12)
        exit = entry + minutes

        qs = self.Price.get_minutes_parked(entry, exit)
        self.assertEqual(qs, 37)


    def test_intervals_to_pay(self):
        interval_0 = self.Price.get_interval_to_pay(7)
        interval_1 = self.Price.get_interval_to_pay(50)
        interval_2 = self.Price.get_interval_to_pay(51)

        self.assertEqual(interval_0, 1)
        self.assertEqual(interval_1, 5)
        self.assertEqual(interval_2, 6)



    # integration
    def test_calc_total_price(self):
        entry_time = datetime.now()

        minutes = timedelta(minutes=37, seconds=12)
        exit_time = entry_time + minutes

        parking = parking_db.objects.create(name="parking_test")
        slot = slot_db.objects.create(size=0, parking_area=parking)


        ticket = ticket_db.objects.create(slot_size=slot, entry_time=entry_time, exit_time=exit_time)
  


        total_price = self.Price.calc_total_price(ticket)

        self.assertEqual(total_price, 48)




