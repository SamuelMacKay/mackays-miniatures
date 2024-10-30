from django.shortcuts import render,  redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Faction

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    products = Product.objects.all()
    query = None
    factions = None

    if request.GET:
        if 'faction' in request.GET:
            factions = request.GET['faction'].split(',')
            products = products.filter(faction__name__in=factions)
            factions = Faction.objects.filter(name__in=factions)


        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('products'))
                
                queries = Q(name__icontains=query) | Q(setting__icontains=query)
                products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_factions': factions
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show specific product details """
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)