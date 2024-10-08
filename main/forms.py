from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["item_name", "category", "price", "topping", "size", "quantity", "description"]

    def clean_item_name(self):
        item_name = self.cleaned_data["item_name"]
        return strip_tags(item_name)

    def clean_category(self):
        category = self.cleaned_data["category"]
        return strip_tags(category)

    def clean_topping(self):
        topping = self.cleaned_data["topping"]
        return strip_tags(topping)
    
    def clean_size(self):
        size = self.cleaned_data["size"]
        return strip_tags(size)
    
    def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)

