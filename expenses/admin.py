from django.contrib import admin
from .models import Expense, Provider

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('provider', 'email', 'phone_number', 'owner')
    search_fields = ('provider', 'owner__username')
    ordering = ('-owner',)

admin.site.register(Expense)
admin.site.register(Provider, ProveedorAdmin)


# Register your models here.
