from django.contrib import admin
from .models import Customer, Restaurants, Menu, Cart
# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurants)
admin.site.register(Menu)
admin.site.register(Cart)