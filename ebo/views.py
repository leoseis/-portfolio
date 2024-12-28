from django.shortcuts import render

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


