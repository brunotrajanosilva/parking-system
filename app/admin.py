from django.contrib import admin
from .models import Ticket, Slot, ParkingArea

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ['token', 'slot_size', 'entry_time', 'exit_time', 'parking_time', 'minutes', 'total_price']
    ordering = ["-entry_time"]

    def parking_time(self, obj):
        entry, exit = obj.entry_time, obj.exit_time

        if entry and exit:
            diff = exit - entry
            # return diff.seconds / 60
            return diff


        return None

    def minutes(self, obj):
        entry, exit = obj.entry_time, obj.exit_time

        if entry and exit:
            diff = exit - entry
            return diff.total_seconds() / 60

        return None

class SlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'size', 'status', 'parking_area']


class ParkingAreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register( Ticket, TicketAdmin)
admin.site.register( Slot, SlotAdmin)
admin.site.register( ParkingArea, ParkingAreaAdmin)