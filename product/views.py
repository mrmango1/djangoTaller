import math
from django.shortcuts import render, get_object_or_404
from .models import Clothes

def roundRating(rating):
    return math.ceil(rating) if rating % 1 >= 0.5 else math.floor(rating)

# Create your views here.

def shop(request):
    clothes = Clothes.objects.all()
    for cloth in clothes:
        cloth.rating_rounded = roundRating(cloth.rating)
    return render(request, "shop.html", {'clothes': clothes})

def shopByBrand(request, brand):
    clothes = Clothes.objects.filter(brand=brand)
    for cloth in clothes:
        cloth.rating_rounded = roundRating(cloth.rating)
    return render(request, "shop.html", {'clothes': clothes})

def shopByCategory(request, category):
    clothes = Clothes.objects.filter(category=category)
    for cloth in clothes:
        cloth.rating_rounded = roundRating(cloth.rating)
    return render(request, "shop.html", {'clothes': clothes})

def shopByGender(request, gender):
    clothes = Clothes.objects.filter(gender=gender)
    for cloth in clothes:
        cloth.rating_rounded = roundRating(cloth.rating)
    return render(request, "shop.html", {'clothes': clothes})

def productDetail(request, id_product):
    cloth = get_object_or_404(Clothes, id=id_product)
    cloth.rating_rounded = roundRating(cloth.rating)
    related_clothes = Clothes.objects.filter(brand=cloth.brand).exclude(id=cloth.id)
    images = cloth.images.all()
    list_images = []
    for i in range(0, len(images), 3):
        list_images.append(images[i:i+4])
    print(list_images)
    for related_cloth in related_clothes:
        related_cloth.rating_rounded = roundRating(related_cloth.rating)
    return render(request, "productDetail.html", {'clothDetail': cloth, 'relatedClothes': related_clothes, 'images': list_images})