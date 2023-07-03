from django.contrib import admin
from .models import *


class ShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price']
    filter_horizontal = ('size',)


admin.site.register(Shoes, ShoesAdmin)
admin.site.register(ShoesSize)
admin.site.register(Customer)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryInformation)
