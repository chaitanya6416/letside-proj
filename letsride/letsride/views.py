from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from tabulate import tabulate

import json

@api_view(["GET"])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer])
def caller(request):
    query ='''
        SELECT 
        A.id, A.name, A.start_location, A.end_location, A.date_of_travel, A.travel_medium, B.id, B.name ,
        (CASE
            WHEN C.id is null THEN "Not Applied"
            ELSE "Applied"
            END) as application_status
        FROM
            rider_rider AS A
                INNER JOIN
            requester_requester AS B ON A.start_location = B.start_location
                AND A.end_location = B.end_location
                AND A.date_of_travel = B.date_of_travel
                LEFT JOIN
    requester_matching AS C ON C.req_id = B.id AND C.rid_id = A.id

    '''
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    headers = ['rider_id','rider_name','rider_start_location','rider_end_location','date_of_travel','travel_medium','requester_id', 'requester_name', 'app_status']
    print(tabulate(results, headers, tablefmt='fancy_grid'))
    return HttpResponse(results )

    

def execute_to_dict(query, params=None):
    with connection.cursor() as c:
        c.execute(query, params or [])
        names = [col[0] for col in c.description]
        return [dict(list(zip(names, values))) for values in c.fetchall()]