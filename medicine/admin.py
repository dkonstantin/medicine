from django.contrib import admin
from medicine.models import Doctor, Visit

class VisitAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_filter = ('doctor', 'datetime')
    list_display = ('name', 'doctor', 'datetime')

admin.site.register(Visit, VisitAdmin)
admin.site.register(Doctor)