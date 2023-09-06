from .models import Info, SocialNetwork

def info(request):
    info = Info.objects.all().order_by('created_at')
    social_networks = SocialNetwork.objects.all().order_by('created_at')
    return {'info': info.values(), 'principalInfo': info.first(), 'social_networks': social_networks.values()}
    