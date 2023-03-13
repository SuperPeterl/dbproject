from django.shortcuts import  render, redirect
#from .forms import NewUserForm
#from django.contrib.auth import login
#from django.contrib import messages


def bill(request):
    return render(request, 'bill.html')