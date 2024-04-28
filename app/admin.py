from django.contrib import admin
from .models import Ticket, Slot

# Register your models here.

class SlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'size', 'status')

admin.site.register( Slot, SlotAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'car_size', 'slot', 'entry_time', 'exit_time', 'price')

    """  def slot(self, obj):
        return 'obj.slot.id' """

admin.site.register( Ticket, TicketAdmin)