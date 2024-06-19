from django.test import TestCase, Client
from django.urls import reverse
from ..models import Slot, ParkingArea, Ticket

from ..views import index, entry, exit

from datetime import datetime


class ViewsClassTestCase(TestCase):
    def setUp(self):
        parking_area = ParkingArea.objects.create(name="test")
        Slot.objects.create(size=0, parking_area=parking_area)

        # self.url = reverse('index', kwargs={'area': 'area-a'})
        self.kwargs = {'area': 'area-a'}


    def test_index(self):
        url = reverse('index')
        response = Client().get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_area(self):
        url = reverse('area', kwargs=self.kwargs)
        response = Client().get(url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'area.html')


    def test_entry(self):
        url = reverse('entry', kwargs=self.kwargs)
        response = Client().post(url, {'car_size': 0})

        self.assertEquals(response.status_code, 201)

    def test_entry_form_not_valid(self):
        url = reverse('entry', kwargs=self.kwargs)
        response = Client().post(url, {'car_ssssize': 0})
        response2 = Client().post(url, {'car_size': 5})

        self.assertEquals(response.status_code, 400)
        self.assertEquals(response2.status_code, 400)


    def test_entry_raises(self):
        url = reverse('entry', kwargs=self.kwargs)
        response = Client().post(url, {'car_size': 3})

        self.assertEquals(response.status_code, 401)


    def test_exit(self):
        url = reverse('exit', kwargs=self.kwargs)
        slot_size = Slot.objects.get(id=1)
        ticket = Ticket.objects.create(slot_size=slot_size)
        token = ticket.token
        
        response = Client().post(url, {'token': token})

        self.assertEquals(response.status_code, 202)
        self.assertTemplateUsed(response, 'exit.html')


    def test_exit_form_not_valid(self):
        url = reverse('exit', kwargs=self.kwargs)
        key_error = Client().post(url, {'tokennnnn': 'token'})
        uuid_error = Client().post(url, {'token': '32q0sk'})

        self.assertEquals(key_error.status_code, 400)
        self.assertEquals(uuid_error.status_code, 400)


    def test_exit_raises(self):
        url = reverse('exit', kwargs=self.kwargs)
        response = Client().post(url, {'token': 'd18b014e-baa4-4638-b33d-e99918986495'})

        self.assertEquals(response.status_code, 401)
    

    


