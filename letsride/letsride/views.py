from django.http import HttpResponse
from django.db import connection
from rest_framework.decorators import api_view
from tabulate import tabulate

@api_view(["GET"])
def list_matching_cases(request):
    query ='''
        SELECT 
        B.id, B.name, A.id, A.name, A.start_location, A.end_location, A.date_of_travel, A.travel_medium ,
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
    headers = ['requester_id', 'requester_name','rider_id','rider_name','start_location','end_location','date_of_travel','travel_medium', 'app_status']
    print(tabulate(results, headers, tablefmt='fancy_grid'))
    return HttpResponse(results )
