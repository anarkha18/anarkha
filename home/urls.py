from django.urls import path
from home import views

urlpatterns = [
    path('asgmnt1', views.assignment1, name="asgmnt1"),
    path('asgmnt2', views.assignment2, name="asgmnt2"),
    path('asgmnt3', views.assignment3, name="asgmnt3"),
    path('asgmnt4', views.assignment4, name="asgmnt4"),
    path('asgmnt5', views.assignment5, name="asgmnt5"),
]
