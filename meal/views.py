from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "Home.html")


# meals show
def meals(request):
    return render(request, "ShowItem.html")
