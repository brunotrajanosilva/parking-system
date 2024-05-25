from .base.Slots import Slots
from .base.Price import Price
from .base.Ticket import Ticket
from .base.Parking import Parking


from ..models import Ticket as ticket_DB
from ..models import Slot as slot_DB


parking_area_a = Parking(
    ticket = Ticket(ticket_DB),
    price = Price( [ 1, 3, 4 ], 10),
    slots = Slots( slot_DB.objects.filter(parking_area__id=1) )
)


parking_area_premium = Parking(
    ticket = Ticket(ticket_DB),
    price = Price( [ 15, 17, 35, 80 ], 60),
    slots = Slots( slot_DB.objects.filter(parking_area__id=2) )
)

list_parking_areas = {
    'area-a': parking_area_a,
    'area-premium': parking_area_premium

}

