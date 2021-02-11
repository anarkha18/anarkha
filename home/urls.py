from django.urls import path
from home import views

urlpatterns = [
    path('asgmnt1', views.assignment1, name="asgmnt1"),
    path('asgmnt2', views.assignment2, name="asgmnt2"),
    path('asgmnt3', views.assignment3, name="asgmnt3"),
    path('asgmnt4', views.assignment4, name="asgmnt4"),
    path('asgmnt5', views.assignment5, name="asgmnt5"),
    path('asgmnt6', views.assignment6, name="asgmnt6"),
    path('asgmnt7', views.assignment7, name="asgmnt7"),
    path('asgmnt8', views.assignment8, name="asgmnt8"),
]
