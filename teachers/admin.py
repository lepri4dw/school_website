from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession']
    search_fields = ['name', 'profession']

admin.site.register(Teacher, TeacherAdmin)


