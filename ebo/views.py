from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def projects (request):
    projects_show=[
        {
            'title': 'EBOs Markets place ',
            'path': 'images/rasoi_connect.PNG',
        },
        {
            'title': 'Chats application',
            'path': 'images/chat.PNG',
        },

        {
            'title': 'NotesApp',
            'path': 'images/note.PNG',
        },
        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },

         {
            'title': 'Photo Uploader',
            'path': 'images/photo_uploader.PNG',
        },
          {
            'title': 'To do list',
            'path': 'images/todolist.PNG',
        },
         {
            'title': 'Portfolio',
            'path': 'images/porto.PNG',
        },
                  {
            'title': 'Labour Hiring',
            'path': 'images\labour_hiring.PNG',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})



def experience(request):
    experience=[
        {"company":"ABC",
         "position":"python developer"},
        {"company":"ABC2",
         "position":"python developer2"},
        {"company":"ABC3",
         "position":"python developer3"}
    ]
    return render (request,"experience.html",{"experience":experience})


def certification(request):
    return render(request, 'certification.html')


def contacts(request):
    return render (request, 'contacts.html')


def resume(request):
    resume_path="myapp/resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)



