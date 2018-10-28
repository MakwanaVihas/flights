from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Flight,Airport,Passengers
# Create your views here.
def index(request):
    context={
    "flights":Flight.objects.all()
    }
    return render(request,"flights/index.html",context)
def flight(request,fid):
    try:
        f=Flight.objects.get(pk=fid)
        context={
        "flights": f,
        "passengers": f.passengers.all(),
        "not_passengers":Passengers.objects.exclude(flight=f).all()
        }
        return render(request,"flights/flight.html",context)
    except Flight.DoesNotExist:
        raise Http404("DNE!!!")
def book(request,fid):
    try:
        passenger_id=int(request.POST['passenger'])
        passenger=Passengers.objects.get(pk=passenger_id)
        flight=Flight.objects.get(pk=fid)
    except Passengers.DoesNotExist:
        return render(request,"flights/error.html",{"message":"Passenger does not exist "})
    except Flight.DoesNotExist:
        return render(request,"flights/error.html",{"message":"Flight does not exist "})
    except KeyError:
        return render(request,"flights/error.html",{"message":"No Selection"})
    passenger.flight.add(flight)
    return HttpResponseRedirect(reverse("flight",args=(fid,)))
