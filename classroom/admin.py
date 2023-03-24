from django.contrib import admin

from classroom.models import *

admin.site.site_header = 'Vacua Admin'
admin.site.site_title = 'Vacua Admin'
admin.site.index_title = 'Vacua Admin'

admin.site.register(Users)
admin.site.register(Department)
admin.site.register(Schools)
admin.site.register(Reservations)
admin.site.register(Buildings)
admin.site.register(Halls)
