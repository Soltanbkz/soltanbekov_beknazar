from django.shortcuts import render
from .models import Price

def index(request):
    prices = Price.objects.all()
    context = {
        'prices': prices,
    }
    return render(request, 'main/index.html', context)