from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks

# Create your views here.

def Home(request):
    tasks = Tasks.objects.all()
    context = {
        'title':"Home",
        'tasks':tasks

    }
    return render(request,'todo/index.html',context)
