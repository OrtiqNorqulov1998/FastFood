from django.contrib import admin
from home.models import Messagess



class MessagessAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'email', 'message']
    list_filter = ['name']


admin.site.register(Messagess, MessagessAdmin)


