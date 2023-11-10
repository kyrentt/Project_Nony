from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Post
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView


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

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detalles_post.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'posts.html'
    fields = '__all__'