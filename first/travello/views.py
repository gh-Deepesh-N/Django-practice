from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination() 
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = True

    dests = [dest1]
    return render(request, "index.html", {'dests': dests})
    


def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def news(request):
    return render(request, "news.html")
def contact(request):
    return render(request, "contact.html")
