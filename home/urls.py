from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("process",views.process,name='process'),
    path("exams",views.exams,name='exams'),
    path("ssb",views.ssb,name='ssb'),
    path("explore",views.explore,name='explore'),
    path("vaibhav",views.vaibhav,name='vaibhav'),
    path("akash",views.akash,name='akash'),
    path("leroy",views.leroy,name='leroy'),
    path("vikas",views.vikas,name='vikas'),
    path("shas",views.shas,name='shas'),
    path("sartaj",views.sartaj,name='sartaj'),
    path("saveupdates",views.saveUpdates,name='saveupdates'),

]