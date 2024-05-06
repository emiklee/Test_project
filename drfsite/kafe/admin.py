from django.contrib import admin
from .models import *


class TablesAdmin(admin.ModelAdmin):
    list_display = ['id', 'num', 'description', 'maxGuests', 'guestsDef', 'guestsNow']
    list_display_links = ['num']
    ordering = ['num', ]
    search_fields = ['num', ]
    fields = ['num', 'description', 'maxGuests', 'guestsDef']
    readonly_fields = ['guestsDef']
    list_per_page = 10


admin.site.register(Tables, TablesAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'isPresent', 'name', 'table']
    list_display_links = ['name']
    list_filter = ['isPresent', 'created', 'updated']
    list_editable = ['isPresent']
    search_fields = ['name', ]
    fields = ['isPresent', 'name', 'table', 'created', 'updated']
    ordering = ['table', ]
    readonly_fields = ['created', 'updated']
    list_per_page = 10


admin.site.register(Guests, GuestAdmin)
admin.site.site_header = 'Административная панель'
