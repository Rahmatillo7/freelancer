from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'payment_method', 'timestamp')
    list_filter = ('status', 'payment_method', 'timestamp')

    search_fields = ('user__username', 'id', 'amount')
    list_editable = ('status',)
    readonly_fields = ('timestamp',)

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('user', 'order', 'amount')
        }),
        ('To\'lov tafsilotlari', {
            'fields': ('status', 'payment_method', 'timestamp')
        }),
    )
    autocomplete_fields = ['user', 'order']