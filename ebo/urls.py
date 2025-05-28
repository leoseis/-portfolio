from django.urls import path
from .views import (
    home,
    about,
    projects,
    experience,
    certification,
    contacts,
    resume,
    contact_view,
    contact_success_view
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("projects/", projects, name="projects"),
    path("experience/", experience, name="experience"),
    path("certification/", certification, name="certification"),
    path("contacts/", contacts, name="contacts"),
    path("resume/", resume, name="resume"),
    path("contact_view/", contact_view, name="contact"),
    path("success/", contact_success_view, name="contact_success"),
]
