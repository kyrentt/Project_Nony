from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Post, e_d, e_g, e_l, e_m, e_o
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-id"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "detalles_post.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts.html"
    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "editar_posts.html"
    # fields = ["titulo", "titulo_post", "cuerpo"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "borrar_posts.html"
    success_url = reverse_lazy("home")


# etiquetas


def etiqueta(request):
    if request.method == "GET":
        de = request.GET.get("Deportista")
        ga = request.GET.get("Gamer")
        ot = request.GET.get("Otaku")
        lg = request.GET.get("LGBTQ")
        mu = request.GET.get("Musica")
        etiqueta = []
        etiqueta.extend([de, ga, ot, lg, mu])
        for k in etiqueta:
            if k == "Deportista":
                e_d(Deportista=k, correo=request.session["mail"]).save()
            elif k == "Gamer":
                e_g(Gamer=k, correo=request.session["mail"]).save()
            elif k == "LGBTQ":
                e_l(LQBTQ=k, correo=request.session["mail"]).save()
            elif k == "Musica":
                e_m(Musica=k, correo=request.session["mail"]).save()
            elif k == "Otaku":
                e_o(Otaku=k, correo=request.session["mail"]).save()
        messages.success(request, "etiquetas guardadas")
        return render(request, "etiquetas.html")
    else:
        return render(request, "etiquetas.html")
