from django import forms
from .models import Product


class ProductEditingForm(forms.Form):
    edited_product = forms.ModelChoiceField(label='Изменяемый товар', queryset=Product.objects.all())
    name = forms.CharField(label='Название', max_length=100, required=False)
    content = forms.CharField(label='Описание', max_length=100, required=False)
    price = forms.DecimalField(label='Цена', max_digits=15, decimal_places=2, required=False)
    count = forms.IntegerField(label='Количество', min_value=0, required=False)
    adding_date = forms.DateField(label='Дата добавления', required=False)
    image = forms.ImageField(label='Изображение', required=False)
