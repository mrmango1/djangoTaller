from django.shortcuts import render
from .models import Carousel

# Create your views here.

def home(request):
    carousel = Carousel.objects.all().order_by('created_at')
    return render(request, "home.html", {'carousel': carousel})
