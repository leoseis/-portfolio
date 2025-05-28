from django.contrib import admin

from .models import ContactMessage

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message','submitted_at')




