from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "type", "sku", "quantity"]

    def clean_sku(self):
        sku = self.cleaned_data.get("sku")
 
        if Product.objects.filter(sku=sku).exists() and not self.instance.pk:
            raise forms.ValidationError("This SKU already exists.")

        return sku
