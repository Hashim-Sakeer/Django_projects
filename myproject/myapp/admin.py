from django.contrib import admin

# Register your models here.
from . models import places
admin.site.register(places)          #register services model to admin panel

from . models import team
admin.site.register(team)
