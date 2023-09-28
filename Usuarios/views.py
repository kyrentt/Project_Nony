from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import *
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def registro(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form =UserCreationForm()
    context={ 'form' : form }
    return render(request, 'registro.html', context)
        