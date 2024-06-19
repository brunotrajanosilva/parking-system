class Slots:

    def __init__(self, slots_db):
        self.slots_db = slots_db


    def get_a_free_slot(self, slot_size):
        try:
            free_slot = self.slots_db.filter(status=False, size__gte=slot_size).order_by('size')[0]
            return free_slot
        
        except Exception as err:
            raise ValueError('cannot find a slot for you')

    def set_slot_available(self, slot):
        slot.status = False
        slot.save()

    def set_slot_unavailable(self, slot):
        slot.status = True
        slot.save()

    def get_all_slots_status(self):
        slots = self.slots_db.all()
        return slots