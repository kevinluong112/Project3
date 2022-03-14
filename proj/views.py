from django.http import HttpResponseRedirect
from django.shortcuts import render
from ClientProfile.forms import ClientProfileForm
from ClientProfile.models import ClientProfileModel



# Create your views here.
def homeview(request, *args, **kwargs):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def clienthome(request, *args, **kwargs):
    #return HttpResponse("<h1>Profile Page</h1>")
    return render(request, "clientmode.html", {})

def profile(request, *args, **kwargs):
    #return HttpResponse("<h1>Profile Page</h1>")
    return render(request, "profile.html", {})

# def fuelQuote(request, *args, **kwargs):
#     #return HttpResponse("<h1>Fuel Quote</h1>")
#     return render(request, "fuelquote.html", {})

def fuelQuote(request, *args, **kwargs):
    if request.method == 'POST':
        form = ClientProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            history = form.cleaned_data['history']
            summary = form.cleaned_data['summary']
            new_client = ClientProfileModel(name, description, price, history, summary)
            new_client.save()
            return HttpResponseRedirect('/register/')
    else:
        form = ClientProfileForm
    return render(request, "fuelquote.html", {'form':form})


def history(request, *args, **kwargs):
    #return HttpResponse("<h1>Fuel Quote History</h1>")
    return render(request, "history.html", {})


def login(request, *args, **kwargs):
    #return HttpResponse("<h1>Login Page</h1>")
    return render(request, "login.html", {})


def register(request, *args, **kwargs):
    return render(request, "register.html", {})

def guestpage(request, *args, **kwargs):
    return render(request, "guessmode.html", {})


