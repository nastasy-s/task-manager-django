from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Position, Worker

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']

@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'is_superuser'
    ]
    list_filter = ['position','is_staff','is_active']

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('position',)}),
    )
