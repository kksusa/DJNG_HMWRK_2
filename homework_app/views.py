from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import User, Order, Product
from datetime import datetime, timedelta
from .forms import ProductEditingForm


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


def get_product_by_id(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    context = {
        'title': 'Продукт',
        'message': 'Описание продукта',
        'product': product,
    }
    return render(request, "homework_app/product.html", context)


def edit_product(request):
    message = 'Товар не заменился'
    if request.method == 'POST':
        form = ProductEditingForm(request.POST, request.FILES)
        if form.is_valid():
            edited_product = form.cleaned_data['edited_product']
            if form.cleaned_data['name']:
                edited_product.name = form.cleaned_data['name']
                message = 'Товар изменён'
            if form.cleaned_data['content']:
                edited_product.content = form.cleaned_data['content'],
                message = 'Товар изменён'
            if form.cleaned_data['price']:
                edited_product.price = form.cleaned_data['price']
                message = 'Товар изменён'
            if form.cleaned_data['count']:
                edited_product.count = form.cleaned_data['count']
                message = 'Товар изменён'
            if form.cleaned_data['adding_date']:
                edited_product.adding_date = form.cleaned_data['adding_date']
                message = 'Товар изменён'
            if form.cleaned_data['image']:
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
                edited_product.image = image
                message = 'Товар изменён'
            if message == 'Товар изменён':
                edited_product.save()
    else:
        message = 'Выберите товар и измените его.'
        form = ProductEditingForm()
    return render(request, 'homework_app/product_editing.html',
                  {'form': form, 'message': message, 'title': 'Изменение товара'})
