from django.contrib import admin
from .models import CustomeUser,medicine

# Register your models here.
admin.site.register(CustomeUser)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(medicine)
# admin.site.register(Prescription, PrescriptionAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
# admin.site.register(Delivery, DeliveryAdmin)
