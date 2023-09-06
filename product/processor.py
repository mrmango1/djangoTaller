from .models import Brand, Category, Clothes
from .views import roundRating

def productInfo(request):
    list_brands = []
    brands = Brand.objects.all().order_by('created_at')
    categories = Category.objects.all().order_by('created_at')
    for i in range(0, len(brands), 4):
        list_brands.append(brands[i:i+4])
    return {'brands': list_brands, 'all_brands': brands, 'categories': categories}

def featured(request):
    featuredClothes = Clothes.objects.all().order_by('-rating')[:3]
    for cloth in featuredClothes:
        cloth.rating_rounded = roundRating(cloth.rating)
    categories = Category.objects.all().order_by('created_at')[:3]
    return {'featuredClothes': featuredClothes, 'categories': categories}