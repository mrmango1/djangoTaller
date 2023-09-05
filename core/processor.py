from .models import Info

def info(request):
    info = Info.objects.all().order_by('created_at')
    print(info.values()[0])
    return {'info': info.values(), 'principalInfo': info.values()[0]}
    