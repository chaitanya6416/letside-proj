from django.shortcuts import render, redirect
from .forms import RiderForm
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import RiderSerializer
from .models import Rider

def index(request):
    return HttpResponse("Hello World from rider") 

@api_view(["POST"])
def rider_form(request):
    if request.method == 'POST':
        serializer = RiderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(["GET"])
def riders_list(request):
    if request.method == 'GET':
        riders = Rider.objects.all()
        serializer = RiderSerializer(riders, many=True)
        return Response(serializer.data)
        