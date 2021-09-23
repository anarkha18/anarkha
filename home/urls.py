from django.urls import path
from home import views

urlpatterns = [
    path('sd', views.sd, name="sd"),
    path('home', views.home, name="home"),
    path('fblogin', views.fblogin, name="fblogin"),
    path('fbhome', views.fbhome, name="fbhome"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('blogs', views.blogs, name="blogs"),
    path('blogposts', views.blogposts, name="blogposts"),
    path('addpost', views.addpost, name="addpost"),
    path('deletepost<int:id>/', views.deletepost, name="deletepost"),
    path('bloppage<str:slug>', views.blogpage, name="blogpage"),
    path('updatepost/<int:id>/', views.updatepost, name="updatepost"),
    path('inbox', views.inbox, name="inbox"),
    path('deletemsg<int:id>/', views.deletemsg, name="deletemsg"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('profile', views.profile, name="profile"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('editprofile', views.editprofile, name="editprofile"),
    # path('profileedit', views.profileedit, name="profileedit"),
    path('settings', views.settings, name="settings"),
    # path('postComment', views.postComment, name="postComment"),
]