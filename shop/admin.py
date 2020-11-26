#pass and username = user1234
from django.contrib import admin
from .models import Product, Contact, Order_place, Subscriber

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order_place)
admin.site.register(Subscriber)