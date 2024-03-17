from django.contrib import admin

from applications.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    search_fields = ['full_name']

admin.site.register(Application, ApplicationAdmin)
