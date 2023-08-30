from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, "shop.html")

def productDetail(request, id_product):
    return render(request, "productDetail.html")