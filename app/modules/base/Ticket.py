
from django.utils import timezone


class Ticket:
    def __init__(self, ticket_db):
        self.ticket_db = ticket_db

    def create_ticket(self, slot_size):
        new_ticket = self.ticket_db(slot_size=slot_size)
        new_ticket.save()
       
        return new_ticket


    def end_ticket(self, token):
        get_ticket = self.ticket_db.objects.get(token=token)
        get_ticket.exit_time = timezone.now()
        get_ticket.save()

        return get_ticket
