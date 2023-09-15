from django.contrib import admin
from .models import User, Product, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    ordering = ['name']
    list_filter = ['name']
    search_help_text = 'Поиск пользователя по имени'
    fields = ['name', 'email', 'phone_number', 'registration']
    readonly_fields = ['name', 'registration']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'price']
    ordering = ['name']
    list_filter = ['name']
    search_help_text = 'Поиск продукта по названию'
    fields = ['name', 'content', 'price', 'count', 'image']
    readonly_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'sum_price', 'order_date']
    ordering = ['-order_date']
    list_filter = ['user_name']
    search_help_text = 'Поиск заказа по пользователю'
    fields = ['user_name', 'products', 'sum_price', 'order_date']
    readonly_fields = ['order_date']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
