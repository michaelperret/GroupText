from django.contrib import admin

# Register your models here.
from letsparty.models import Partier, Event, Address

admin.site.register(Partier)
admin.site.register(Event)
admin.site.register(Address)