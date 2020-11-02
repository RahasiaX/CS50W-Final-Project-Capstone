from django.contrib import admin
from .models import Shoe, ShoeSize, ShoeImage, ShoeColor, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Shoe)
admin.site.register(ShoeSize)
admin.site.register(ShoeImage)
admin.site.register(ShoeColor)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)