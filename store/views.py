from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# create new
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "store/product_form.html", {"form": form})
# all list
def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})

# update
def update_product(request, sku):
    product = get_object_or_404(Product, sku=sku)
    
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "store/product_form.html", {"form": form, "product": product})

def create_or_update_product(request, sku=None):
    product = None

    if sku:
        product = get_object_or_404(Product, sku=sku)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "store/product_form.html", {"form": form, "product": product})

def delete_product(request, sku):
    product = get_object_or_404(Product, sku=sku)
    product.delete()  
    return redirect("product_list")   