from django.shortcuts import render
from django.http import HttpResponse
from .forms import EntryCar, TicketNumber

from .modules.parking_system import parking_system
from django.views.decorators.csrf import csrf_exempt
from .models import Slot

# Create your views here.

@csrf_exempt
def index(request):
    slots = Slot.objects.all()
    

    context = {}
    context['entry_car'] = EntryCar()
    context['ticket_number'] = TicketNumber()
    context['slots'] = slots


    return render(request, 'index.html', context)


@csrf_exempt
def entry(request):
    parking = parking_system()
    slots = Slot.objects.all().values()


    context = {
        'slots': slots 
    }

    if request.method == "POST":

        entry_car = EntryCar(request.POST)

        if entry_car.is_valid():
            
            ticket = parking.entry(request.POST['car_size'])

            for slot in slots:
                if slot['id'] == ticket.slot.id:
                    slot['active'] = True
            
            context = {
                'ticket': ticket,
                'slots': slots 
            }

            return render(request, 'entry.html', context)

        else:
            return HttpResponse('form is not valid.')

    else:
        

        return render(request, 'entry.html', context)


@csrf_exempt
def exit(request):
    if request.method == "POST":

        ticket_number = TicketNumber(request.POST)

        if ticket_number.is_valid():

            parking = parking_system()
            ticket = parking.exit(request.POST['ticket_number'])

            return HttpResponse(f'total to pay: {ticket.price}')

