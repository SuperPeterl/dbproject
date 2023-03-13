from django.shortcuts import  render, redirect
#from .forms import NewUserForm
#from django.contrib.auth import login
#from django.contrib import messages


def employee(request):
    return render(request, 'employee.html')