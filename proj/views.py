from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeview(request, *args, **kwargs):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def clienthome(request, *args, **kwargs):
    #return HttpResponse("<h1>Profile Page</h1>")
    return render(request, "ClientProfile/clientmode.html", {})
