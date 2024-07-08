from django.shortcuts import render
from .models import Product  # Adjust based on your actual model name

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def home(request):
    return render(request, 'home.html')
