from django.http import HttpResponse
from django.shortcuts import render
from folio2.models import skills, projects, aboutme

def home(request):
    skillsdata=skills.objects.all()
    projectdata=projects.objects.all()
    aboutmedata=aboutme.objects.all()
    data={
        'skillsdata':skillsdata,
        'projectdata':projectdata,
        'aboutmedata':aboutmedata,
    }
    return render(request,"index.html",data)
def about(request):
    aboutmedata=aboutme.objects.all()
    data={
        'aboutmedata':aboutmedata
    }
    return render(request,"about.html",data)
def skill(request):
    skillsdata=skills.objects.all()
    data={
        'skillsdata':skillsdata
    }
    return render(request,"skills.html",data)
def project(request):
    projectdata=projects.objects.all()
    data={
        'projectdata':projectdata
    }
    return render(request,"project.html",data)        