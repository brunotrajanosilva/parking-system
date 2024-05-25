class Parking:
    def __init__(self, ticket, price, slots):
        self.ticket = ticket
        self.price = price
        self.slots = slots


    def get_slots(self):
        return self.slots.get_all_slots_status()

    def entry(self, slot_size):
        free_slot = self.slots.get_a_free_slot(slot_size)

        if free_slot:
            new_ticket = self.ticket.create_ticket(free_slot)
            self.slots.set_slot_unavailable(free_slot)
            
            return new_ticket



    def exit(self, token):

        end_ticket = self.ticket.end_ticket(token)
        self.slots.set_slot_available(end_ticket.slot_size)

        total_price = self.price.calc_total_price(end_ticket)

        end_ticket.total_price = total_price
        end_ticket.save()

        return end_ticket