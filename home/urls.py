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
    path('asgmnt9', views.assignment9, name="asgmnt9"),
    path('asgmnt10', views.assignment10, name="asgmnt10"),
    path('asgmnt11', views.assignment11, name="asgmnt11"),
    path('asgmnt12', views.assignment12, name="asgmnt12"),
    path('asgmnt13', views.assignment13, name="asgmnt13"),
    path('asgmnt14', views.assignment14, name="asgmnt14"),
    path('asgmnt15', views.assignment15, name="asgmnt15"),
    path('asgmnt16', views.assignment16, name="asgmnt16"),
    path('bootstrap1', views.bootstrap1, name="bootstrap1"),
    path('bootstrap2', views.bootstrap2, name="bootstrap2"),
    path('fbhome', views.fbhome, name="fbhome"),
    path('validate', views.validate, name="validate"),
]