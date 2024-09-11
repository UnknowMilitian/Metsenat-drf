from django.contrib import admin
from .models import Payment, User


# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class PaymentAdmin(admin.ModelAdmin):
    pass
