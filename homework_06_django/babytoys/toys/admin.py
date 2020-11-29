from django.contrib import admin
from .models import Category, Card, Images, OrderItem, Order

admin.site.register(Card)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(OrderItem)
admin.site.register(Order)

# Register your models here.
