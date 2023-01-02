from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RequesterSerializer, MatchingSerializer
from .models import Requester, Matching
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("Hello World from requester")


@api_view(["POST"])
def requester_form(request):
    if request.method == 'POST':
        serializer = RequesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["GET"])
def requester_list(request):
    if request.method == 'GET':
        requesters = Requester.objects.all()

        if asset_type := request.GET.get('asset_type'):
            requesters = requesters.filter(
                asset_type=asset_type)
        if status := request.GET.get('status'):
            requesters = requesters.filter(status=status)

        requesters = requesters.order_by('date_of_travel')
        
        paginator_size = 10
        if custom_paginator_size := request.GET.get('paginator_size'):
            paginator_size = custom_paginator_size
        paginator = Paginator(requesters, paginator_size)
        page = request.GET.get('page')

        serializer = RequesterSerializer(paginator.get_page(page), many=True)

        return Response(serializer.data)


@api_view(["POST"])
def requester_apply_to_rider(request):
    if request.method == 'POST':
        serializer = MatchingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
