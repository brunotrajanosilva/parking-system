import math

class Price:

    def __init__(self, prices, interval):
        self.prices = prices
        self.interval = interval



    def get_price_by_size(self, slot_size):
        price_per_minute = self.prices[slot_size]
        return price_per_minute

    def get_minutes_parked(self, entry, exit):
        diff = exit - entry
        diff_minutes = diff.total_seconds() / 60
        diff_minutes = math.floor(diff_minutes)

        return diff_minutes

    def get_interval_to_pay(self, minutes):
        time_to_pay = minutes / self.interval
        time_to_pay = math.ceil(time_to_pay)
        return time_to_pay



    def calc_total_price(self, ticket):
        slot_size = ticket.slot_size.size

        price_per_minute = self.get_price_by_size(slot_size)
        
        entry, exit = ticket.entry_time, ticket.exit_time

        minutes_parked = self.get_minutes_parked(entry, exit)
        interval_to_pay = self.get_interval_to_pay(minutes_parked)


        total_price = price_per_minute * interval_to_pay

        return total_price