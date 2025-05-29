from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Contact


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    projects_show = [
        {'title': "EBO's Marketplace", 'path': 'images/rasoi_connect.PNG'},
        {'title': 'Chats Application', 'path': 'images/chat.PNG'},
        {'title': 'NotesApp', 'path': 'images/note.PNG'},
        {'title': 'CRUD', 'path': 'images/CRUD.PNG'},
        {'title': 'Photo Uploader', 'path': 'images/photo_uploader.PNG'},
        {'title': 'To Do List', 'path': 'images/todolist.PNG'},
        {'title': 'Portfolio', 'path': 'images/porto.PNG'},
        {'title': 'Labour Hiring', 'path': 'images/labour_hiring.PNG'},
    ]
    return render(request, "projects.html", {"projects_show": projects_show})


def experience(request):
    experience = [
        {"company": "AD Digital", "position": "Python Developer", "year": "Present"},
        {"company": "BGP", "position": "Full Stack Developer", "year": "2021"},
        {"company": "Datavise", "position": "Python Developer", "year": "Until 2019"},
    ]
    return render(request, "experience.html", {"experience": experience})


def certification(request):
    return render(request, 'certification.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('msg', '').strip()

        if name and email and message:
            Contact.objects.create(name=name, email=email, phone=phone, message=message)
            messages.success(request, "Thank you for contacting us!")
            return redirect('contacts')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'contacts.html')


def resume(request):
    resume_path = "myapp/resume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)
