from django.shortcuts import render,redirect


products = [
    {'id': 1, 'name': 'Laptop', 'price': 25000},
    {'id': 2, 'name': 'Mouse', 'price': 500},
    {'id': 3, 'name': 'Keyboard', 'price': 1000},
]


def landing_page(request):
    return render(request, 'product/landing_page.html')

    
def product_list(request):
    return render(request, '/Users/sunflower/Desktop/wa/webdev/djangoPJ/symite/product/templates/product/product_list.html', {'products': products})
