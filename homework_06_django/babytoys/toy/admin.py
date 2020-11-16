from django.contrib import admin
from .models import Category, Card, Element, Images

admin.site.register(Card)
admin.site.register(Category)
admin.site.register(Element)
admin.site.register(Images)

# Register your models here.
