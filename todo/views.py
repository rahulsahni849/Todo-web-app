import logging
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, UpdateView,CreateView
from .models import Tasks
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tasks

# Create your views here.
@login_required
def Home(request):
    if(request.user.is_authenticated):
        user = request.user.username
        #print(user)
        return redirect('todo-home',username=user)
    return redirect('login')

class TaskListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = Tasks
    context_object_name = "tasks"

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))    
        #print(Tasks.objects.filter(user=user).order_by('-created_at'))
        return Tasks.objects.filter(user=user).order_by('-created_at')
    
    def test_func(self):
        user = get_object_or_404(User,username = self.kwargs.get('username')) 
        
        if(self.request.user == user):
            #print(user)
            return True
        return False

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = ["title"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo-home',kwargs = {"username":self.request.user.username})


class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Tasks
    fields = ["title"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo-home',kwargs = {"username":self.request.user.username})

    def test_func(self):
        user = self.get_object()
        print(user.user)
        if(self.request.user == user.user):
            return True
        return False


class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Tasks
    def get_success_url(self):
        return reverse('todo-home',kwargs = {"username":self.request.user.username})

    def test_func(self):
        user = self.get_object()
        if(self.request.user.username == user.user.username):
            print('yes i am')
            return True
        return False




