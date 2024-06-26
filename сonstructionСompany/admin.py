from django.contrib import admin
from django.contrib.auth.models import Permission

from сonstructionСompany.models import *

# Register your models here.
admin.site.register(Address)
admin.site.register(Personnel)
admin.site.register(Project)
admin.site.register(Order)
admin.site.register(Material)
admin.site.register(Warehouse)
admin.site.register(Permission)