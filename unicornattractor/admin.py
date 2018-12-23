from django.contrib import admin
from accounts.models import Item
from tickets.models import Bugs, Features


admin.site.register(Item)
admin.site.register(Bugs)
admin.site.register(Features)