from django import forms


car_choices = (
    (0, 'SM'),
    (1, 'MD'),
    (2, 'LG'),
    (3, 'XL'),
)

class EntryForm(forms.Form):
    car_size = forms.ChoiceField( label="Car Size", widget=forms.RadioSelect, choices=car_choices)

class ExitForm(forms.Form):
    token = forms.UUIDField()