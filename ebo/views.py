from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import messages



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
        {"company":"AD digital",
         "position":"python developer",
         "year":"till date" },
         
        {"company":"BGP",
         "position":"Full stack Dveloper",
         "year":"2021"},
        {"company":"Datavise",
         "position":"python developer3",
         "year":"till 2019"},
    ]
    return render (request,"experience.html",{"experience":experience})


def certification(request):
    return render(request, 'certification.html')




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contacts(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('msg', '').strip()

        # Debugging: Print the form data
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")

        # Validate required fields
        if name and email and message:
            # Save data to the database
            Contact.objects.create(name=name, email=email, phone=phone, message=message)
            messages.success(request, "Thank you for contacting us!")
            return redirect('contacts')  # Redirect to the same page or a 'success' page
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'contacts.html')

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
