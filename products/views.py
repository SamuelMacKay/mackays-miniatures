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
    pre_order = None
    new_releases = None
    specials = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'new_releases' in request.GET:
            new_releases = request.GET['new_releases']
            products = products.filter(is_new=True)

        if 'pre_order' in request.GET:
            pre_order = request.GET['pre_order']
            products = products.filter(pre_order=True)
        
        if 'specials' in request.GET:
            specials = request.GET['specials']
            products = products.filter(
                pre_order=True,
                is_new=True
            )

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_factions': factions,
        'pre_order': pre_order,
        'new_releases': new_releases,
        'specials': specials,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show specific product details """
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)