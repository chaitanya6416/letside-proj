from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('rider_form/', views.rider_form),
    path('riders_list/', views.riders_list)

]
