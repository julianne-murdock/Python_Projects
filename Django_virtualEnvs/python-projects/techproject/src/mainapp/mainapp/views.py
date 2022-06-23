from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = {"Stickers", "Apparel", "Rising Horizons Journal", "Coloring Books", "Decorated Bibles"}
    context = {
        'products': products,
    }

    return render(request, "home.html", context)
