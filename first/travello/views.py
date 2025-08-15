from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()  # Fetch all Destination objects
    return render(request, "index.html", {'dests': dests})
    


def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def news(request):
    return render(request, "news.html")
def contact(request):
    return render(request, "contact.html")
