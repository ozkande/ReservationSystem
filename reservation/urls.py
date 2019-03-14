from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'reservation-home'),
    path('dateselected', views.datetimecheckpage, name = 'datetimecheckpage'),

]