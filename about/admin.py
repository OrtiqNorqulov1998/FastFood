from django.contrib import admin
from about.models import About, Chef


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status']
    list_filter = ['title']

class ChefAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']
    list_filter = ['name']


admin.site.register(About, AboutAdmin)
admin.site.register(Chef, ChefAdmin)