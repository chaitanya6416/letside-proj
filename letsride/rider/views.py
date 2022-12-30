from django.shortcuts import render, redirect
from .forms import RiderForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World from rider") 

def rider_form(request):
    if request.method == 'POST':
        form = RiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        form = RiderForm()
    return render(request, 'rider_form.html', {'form': form})