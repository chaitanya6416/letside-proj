from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('requester_form/', views.requester_form),
    path('requester_list/', views.requester_list),
    path('apply/', views.requester_apply_to_rider)
]
