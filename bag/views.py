from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return to the shopping cart page """
    
    return render(request, 'bag/bag.html')