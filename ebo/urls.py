
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("experience/",views.experience,name="experience"),
    path("certification/",views.certification,name="certification"),
    path("contacts/",views.contacts,name="contacts"),
    path("resume/",views.resume,name="resume"),

]