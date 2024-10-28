from django.contrib import admin
from .models import Client, Writer, Order, Message, CustomUser


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "email")


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_display = ("username", "email", "profile_rating")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("status",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ("subject",)
    list_display = ("subject", "sender", "created_at")


admin.site.register(CustomUser)
