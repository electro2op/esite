from django.shortcuts import render
from ewebapp.models import Product
from django.db.models import Q

# Create your views here.
def Search_Result(request):
    products = None
    query = None
    if 'q' in request.GET:  # Fixed the syntax error here
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})