from django.contrib import admin

from applications.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number']
    search_fields = ['full_name', 'phone_number']

admin.site.register(Application, ApplicationAdmin)
