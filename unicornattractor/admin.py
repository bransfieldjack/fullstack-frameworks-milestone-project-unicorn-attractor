from django.contrib import admin
from accounts.models import Item
from tickets.models import Bugs, Features, Comments
from accounts.models import Profile


admin.site.register(Item)
admin.site.register(Bugs)
admin.site.register(Features)
admin.site.register(Profile)
admin.site.register(Comments)