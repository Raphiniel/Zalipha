from django.contrib import admin

from .models import Category, Item, Conversation, ConversationMessages, OrderItem


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Conversation)
admin.site.register(ConversationMessages)
admin.site.register(OrderItem)
# Register your models here.
