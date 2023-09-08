from django.shortcuts import render
from .models import User, Order
from datetime import datetime, timedelta


def get_orders_by_user_id(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(user_name_id=user)
    orders_with_products = {}
    for order in orders:
        products = Order.objects.get(id=order.id).products.all()
        orders_with_products[order] = products

    context = {
        'user': user,
        'orders': orders_with_products,
    }
    return render(request, "homework_app/orders.html", context)


def get_products_by_user_id(request, user_id: int, period: str):
    user = User.objects.filter(pk=user_id).first()
    current_time = datetime.now()
    if period.lower() == 'hour':
        time_filter = current_time - timedelta(hours=1)
    elif period.lower() == 'week':
        time_filter = current_time - timedelta(weeks=1)
    elif period.lower() == 'month':
        time_filter = current_time - timedelta(days=30)
    elif period.lower() == 'year':
        time_filter = current_time - timedelta(days=365)

    orders = Order.objects.filter(user_name_id=user, order_date__gte=time_filter)
    products = []

    for order in orders:
        products.extend(Order.objects.get(id=order.id).products.all())

    context = {
        'user': user,
        'products': set(products),
    }
    return render(request, "homework_app/products.html", context)
