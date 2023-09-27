from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
from django.shortcuts import render

def login(request):
    return render(request, "login.html")