from django.test import TestCase
from ..models import Slot, ParkingArea
from ..modules.base.Slots import Slots


class SlotClassTestCase(TestCase):

    def setUp(self):
        # create a parking area and his slots
        parking_area = ParkingArea.objects.create(name='parking_area_test')


        for size in range(4):
            Slot.objects.create(size=size, parking_area=parking_area)
            Slot.objects.create(size=size, parking_area=parking_area)

        self.slots = Slots(Slot.objects)


    # get slot by size
    def test_get_slot_by_size(self):

        free_slot_0 = Slot.objects.filter(size=0).first()
        free_slot_1 = Slot.objects.filter(size=1).first()

        get_free_slot_0 = self.slots.get_a_free_slot(0)
        get_free_slot_1 = self.slots.get_a_free_slot(1)

        self.assertTrue(isinstance(get_free_slot_0, Slot))
        self.assertTrue(isinstance(get_free_slot_1, Slot))

        self.assertEqual(get_free_slot_0, free_slot_0)
        self.assertEqual(get_free_slot_1, free_slot_1)



    # get second slot because the first slot is unavailable
    def test_get_second_slot_by_same_size(self):
       
        # set first slots as unavailable
        disable_first_slot_0 = Slot.objects.filter(size=0).first()
        disable_first_slot_0.status = True
        disable_first_slot_0.save()

        disable_first_slot_1 = Slot.objects.filter(size=1).first()
        disable_first_slot_1.status = True
        disable_first_slot_1.save()     

        # select second slots in db
        free_slot_0 = Slot.objects.filter(size=0)[1]
        free_slot_1 = Slot.objects.filter(size=1)[1]

        # should return second slots
        get_free_slot_0 = self.slots.get_a_free_slot(0)
        get_free_slot_1 = self.slots.get_a_free_slot(1)

        self.assertTrue(isinstance(get_free_slot_0, Slot))
        self.assertTrue(isinstance(get_free_slot_1, Slot))

        self.assertEqual(get_free_slot_0, free_slot_0)
        self.assertEqual(get_free_slot_1, free_slot_1)


    # get next size slot
    def test_get_next_size_slot(self):
      
        # disable all slots of size 0 
        Slot.objects.filter(size=0).update(status=True)

        # select first size 1
        free_slot = Slot.objects.filter(size=1).first()


        get_free_slot = self.slots.get_a_free_slot(0)

        self.assertTrue(isinstance(get_free_slot, Slot))
        self.assertEqual(get_free_slot, free_slot)




    # get null with all slots unavailable
    def test_all_slots_unavailable(self):

        # disable all slots of size 0 
        Slot.objects.filter(size=3).update(status=True)


        with self.assertRaises(IndexError):
            # assert a raise when try to select where all slots is disable
            slot_unavailable = self.slots.get_a_free_slot(3)
        
    def test_set_slot_available(self):
        slot = Slot.objects.get(id=1)
        slot.status = True
        slot.save()
        self.slots.set_slot_available(slot)
        
        self.assertFalse(slot.status)


    def test_set_slot_unavailable(self):
        slot = Slot.objects.get(id=1)
        self.slots.set_slot_unavailable(slot)

        self.assertTrue(slot.status)