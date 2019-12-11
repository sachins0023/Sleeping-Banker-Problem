from django.contrib import admin
from .models import User, Session
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("mobile_number", "user_name",)
    
admin.site.register(User, UserAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ("session_key", "user", "user_agent", "ip_address", "active")
    
admin.site.register(Session, SessionAdmin)