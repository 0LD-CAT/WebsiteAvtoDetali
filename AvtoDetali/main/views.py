from django.shortcuts import render
from .models import Details
# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def catalog(request):
    details = Details.objects.all()
    return render(request, 'main/catalog.html', {'details' : details})

def contacts(request):
    return render(request, 'main/contacts.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def news(request):
    return render(request, 'main/news.html')