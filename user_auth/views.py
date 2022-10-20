from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    title = "User Registeration Form"
    if(request.method=="POST"):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Successfully Created!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form':form,
        'page_title':title,
    }
    return render(request,"user_auth/register.html",context)

