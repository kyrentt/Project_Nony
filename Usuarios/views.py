from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Post,persona, e_d, e_g, e_l, e_m, e_a,e_pg,e_c,e_jm,e_k,e_p,e_pp,e_s,e_t,amigos
from django.template import Template, Context
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
import re


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
    if request.method == 'GET': 
            de=request.GET.get('Deportista')
            ga=request.GET.get('Gamer')
            ot=request.GET.get('Anime')
            lg=request.GET.get('LGBTQ')
            mu=request.GET.get('Música')
            tg=request.GET.get('Tecnología')
            jm=request.GET.get('jm')
            ep=request.GET.get('ep')
            so=request.GET.get('Soltero')
            ci=request.GET.get('Cinéfilo')
            kp=request.GET.get('Kpop')
            pp=request.GET.get('pp')
            pg=request.GET.get('pg')
            etiqueta=[]
            etiqueta.extend([de, ga, ot, lg, mu, tg, jm, ep, so, ci, kp, pp, pg])
            for k in etiqueta:
                  if k == 'Deportista':
                        e_d(Deportista=k, correo=request.session['mail']).save()
                  elif k=='Gamer':
                        e_g(Gamer=k, correo=request.session['mail']).save()
                  elif k=='LGBTQ':
                        e_l(LGBTQ=k, correo=request.session['mail']).save()
                  elif k=='Musica':
                              e_m(Música=k, correo=request.session['mail']).save()
                  elif k=='Anime':
                        e_a(Anime=k, correo=request.session['mail']).save()
                  elif k=='Tecnología':
                        e_t(Tecnología=k, correo=request.session['mail']).save()
                  elif k=='Juegos de Mesa':
                        e_jm(jm=k, correo=request.session['mail']).save()
                  elif k=='En pareja':
                        e_p(ep=k, correo=request.session['mail']).save()
                  elif k=='Soltero/a':
                        e_s(Soltero=k, correo=request.session['mail']).save()
                  elif k=='Cinéfilo':
                        e_c(Cinéfilo=k, correo=request.session['mail']).save()
                  elif k=='Kpop':
                        e_k(Kpop=k, correo=request.session['mail']).save()
                  elif k=='Persona de perros':
                        e_pp(pp=k, correo=request.session['mail']).save()
                  elif k=='Persona de gatos':
                        e_pg(pg=k, correo=request.session['mail']).save()
            return render(request, 'etiquetas.html')
    else:
          return render(request, 'etiquetas.html')

#reco,eti:
def ayu(a,c,cor):
     b=[]
     resultado=[]
     d=int(0)
     for l in a:
          p=l.objects.all()
          if p!='':
               j=c[d]
               if d==6:
                  j="jm"
               if d==7:
                  j='ep'
               if d==8:
                  j='Soltero'
               if d==11:
                  j='pp'    
               if d==12:
                  j='pg'
               b.append(l.objects.filter(correo=cor).values_list(j))
          d+=1
     resultado = [queryset.first()[0] for queryset in b if queryset and queryset.first()[0] in c]
     return resultado

#PERFIL
def perfil(request, username=None):
      cor=request.session.get('mail')
      nom=persona.objects.filter(mail=cor).values_list('nombre')
      a=[e_d, e_g, e_l, e_m, e_a,e_t,e_jm,e_p,e_s,e_c,e_k,e_pp,e_pg]
      c=['Deportista', 'Gamer', 'LGBTQ','Música', 'Anime', 'Tecnología' ,'Juegos de Mesa', 'En pareja', 'Soltero/a', 'Cinéfilo', 'Kpop', 'Persona de perros', 'Persona de gatos']
      resultado=ayu(a,c,cor)
      nom = nom[0][0] if nom else None
      if resultado==[]:
          y='Escoje tus primeras etiquetas en "Etiquetas"'
      else:
          y=''
      #Personas en la app
      t=persona.objects.all().values_list('nombre')
      t=[nombre[0] for nombre in t]
      for r in t:
           if r==nom:
                t.remove(nom)
      #%de similitud:
      f=[]
      for g in t:
        i=[]
        eti_simi=''
        por=''
           #acá obtengo el correo de las otras personas
        u=persona.objects.filter(nombre=g).values_list('mail')
        u=u[0][0] if u else None
           #teniendo el correo, obtengo sus listas de etiquetas
        i=ayu(a,c,u)
           #Etiquetas similares
        eti_simi=set(resultado)&set(i)
           #porcentaje de etiquetas en común, considerando que el máximo son 13 etiquetas
        por=str(round((len(eti_simi)/len(set(resultado+i)))*100))
           #creo la lista de nombres con el porcentaje de similitud y nombre
        f.append(g+' '+por+'%')
      f_separada = [(nombre[:-3], int(nombre[-3:-1])) for nombre in f]
      f_ordenada = sorted(f_separada, key=lambda x: x[1], reverse=True)
      f_final = [f"{nombre}{porcentaje}%" for nombre, porcentaje in f_ordenada]
      return render(request, 'perfil.html', {'k':resultado, 'o':nom, 'i': cor, 'y':y, 'f':y, 'e':f_final}) 

#otro perfil
def perfil2(request, name):
     match=re.match(r'([^0-9]+)\s\d+%', name)
     a=match.group(1)
     cor=persona.objects.filter(nombre=a).values_list('mail')
     co=cor[0][0] if cor else None
     j=[e_d, e_g, e_l, e_m, e_a,e_t,e_jm,e_p,e_s,e_c,e_k,e_pp,e_pg]
     c=['Deportista', 'Gamer', 'LGBTQ','Música', 'Anime', 'Tecnología' ,'Juegos de Mesa', 'En pareja', 'Soltero/a', 'Cinéfilo', 'Kpop', 'Persona de perros', 'Persona de gatos']
     eti=ayu(j,c,co)
     return render(request, 'perfil - copia.html', {'i':a, 'a': cor, 'e':eti})
