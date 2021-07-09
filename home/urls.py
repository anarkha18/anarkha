from django.urls import path
from home import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('fblogin', views.fblogin, name="fblogin"),
    path('fbhome', views.fbhome, name="fbhome"),
    path('contact', views.contact, name="contact"),
    path('blogs', views.blogs, name="blogs"),
    path('blogposts', views.blogposts, name="blogposts"),
    path('addpost', views.addpost, name="addpost"),
    path('deletepost<int:id>/', views.deletepost, name="deletepost"),
    path('bloppage<str:slug>', views.blogpage, name="blogpage"),
    path('updatepost/<int:id>/', views.updatepost, name="updatepost"),
    path('messages', views.messages, name="messages"),
    path('deletemsg<int:id>/', views.deletemsg, name="deletemsg"),
    # path('vlog', views.vlog, name="vlog"),
    # path('vsignup', views.vsignup, name="vsignup"),
]