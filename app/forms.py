from django import forms


car_choices = (
    (1, 'SM'),
    (2, 'MD'),
    (3, 'LG'),
    (4, 'XL'),
)

class EntryCar(forms.Form):
    car_size = forms.ChoiceField( label="Car Size", widget=forms.RadioSelect, choices=car_choices)

class TicketNumber(forms.Form):
    ticket_number = forms.CharField(max_length=4)