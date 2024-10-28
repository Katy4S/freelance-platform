from django.contrib import admin
from models import CustomUser, Writer, Client, Order, Message

# Register the models
admin.site.register(CustomUser)
admin.site.register(Writer)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Message)
