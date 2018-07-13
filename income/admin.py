from django.contrib import admin
from .models import Cliente, Income

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('client', 'email', 'phone_number', 'owner')
    search_fields = ('client', 'owner__username')
    ordering = ('-owner',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Income)
