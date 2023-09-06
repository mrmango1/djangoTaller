from .models import Brand

def brand(request):
    list_brands = []
    brands = Brand.objects.all().order_by('created_at')
    for i in range(0, len(brands), 4):
        list_brands.append(brands[i:i+4])
    return {'brands': list_brands}