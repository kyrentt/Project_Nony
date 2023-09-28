from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
from django.shortcuts import render


def home(request):
    return render(request, "home.html")