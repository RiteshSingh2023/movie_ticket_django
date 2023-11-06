from django.urls import path
from film import views

urlpatterns = [
    path('',views.index,name="index"),
    path('adminregister',views.adminregister,name="adminregister"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('admi',views.admi,name="admi"),
    path('addmovie',views.addmovies,name="addmovies"),
    path('logout',views.handlelogout,name="handlelogout"),
    path('userlogi',views.userlogi,name="userlogi"),
    path('usersignup',views.usersignup,name="usersignup"),
    path('customer',views.customer,name="customer"),
    path('ticket',views.ticket,name="ticket"),
    path('book/<id>',views.book,name="book"),
    path('total',views.total,name="total"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
]
