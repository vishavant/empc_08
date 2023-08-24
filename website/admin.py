from django.contrib import admin
from .models import ContactUs, JoinUs


# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'query_type', 'message', 'created_at']


@admin.register(JoinUs)
class JoinUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'qualification', 'city', 'state', 'applied_for', 'resume_file', 'created_at']