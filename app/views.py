from .modules.ParkingAreas import  list_parking_areas


from django.http import HttpResponse
from django.shortcuts import render
from .forms import EntryForm, ExitForm



def index(request, area):
    parking_urls = list_parking_areas.keys()
    parking_area = list_parking_areas[area]
    slots_status = parking_area.get_slots()


    context = {
        'entry': EntryForm(),
        'exit': ExitForm(),
        'urls': parking_urls,
        'slots': slots_status
    }

    return render(request, 'index.html', context)


def entry(request, area):
    parking_area = list_parking_areas[area]
 
    if request.method == 'POST':
        entry_form = EntryForm(request.POST)

        message = ""

        if entry_form.is_valid():
            car_size = request.POST['car_size']

            try:
                new_ticket = parking_area.entry(car_size)
                message = f'new ticket was created: {new_ticket.token}'

                return HttpResponse(content=message, status=201)

            except Exception as ex:
                message =  f'there is an exception: {ex}'
                return HttpResponse( content=message, status=401 )
                

        else:
            message = 'form is not valid'
            return HttpResponse(content=message, status=400)


def exit(request, area):
    parking_area = list_parking_areas[area]
    
    if request.method == 'POST':
        exit_form = ExitForm(request.POST)

        if exit_form.is_valid():
            token = request.POST['token']

            try:
                exit_ticket = parking_area.exit(token)

                context = {
                    'ticket': exit_ticket
                }

                return render(request, 'exit.html', context, status=202)

            except Exception as ex:
                return HttpResponse(content=f'there is an exception: {ex}', status=401)

        else:
            return HttpResponse(content="form is not valid", status=400)
