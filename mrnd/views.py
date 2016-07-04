from django.conf.locale import id
from django.shortcuts import *

# Create your views here.
from mrnd.models import *
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

def index(request):
    return render(request,'home.html')

def home(requset):
    return render(requset,'index.html')

def text(request,location):
    colleges=College.objects.all().filter(location__iexact=location)
    templete=loader.get_template("text.html")
    result=templete.render(context={"colleges":colleges})
    return HttpResponse(result)


def college_details_id(request,id):
    colleges = College.objects.all().get(pk=id)
    students= colleges.student_set.all()
    templete = loader.get_template("college.html")
    result = templete.render(context={"students":students,"college":colleges})
    return HttpResponse(result)

def college_details_acronym(request,acronym):
    colleges = College.objects.all().get(Acronym=acronym)
    students= colleges.student_set.all()
    templete = loader.get_template("college.html")
    result = templete.render(context={"students":students,"college":colleges})
    return HttpResponse(result)