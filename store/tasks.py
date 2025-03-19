from celery import shared_task
from .models import Product

@shared_task
def add_product_task(name, type, sku, quantity):
    """Celery task to add a product asynchronously."""
    product = Product.objects.create(name=name, type=type, sku=sku, quantity=quantity)
    return f"Product {name} added successfully"
