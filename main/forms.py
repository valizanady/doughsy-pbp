from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["item_name", "category", "price", "topping", "size", "quantity", "description"]