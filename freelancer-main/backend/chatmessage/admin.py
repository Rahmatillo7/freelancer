from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'timestamp', 'read_status')
    list_filter = ('read_status', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'message')
    # search_fields borligi uchun autocomplete ishlaydi