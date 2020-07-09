from django.contrib import admin

# Register your models here.
from core.models import User, Customer, Address

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Address)
