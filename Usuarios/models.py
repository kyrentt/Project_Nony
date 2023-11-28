from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    pas = models.CharField(max_length=10)


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_post = models.CharField(max_length=255, default="USMessage")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha_post = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + " | " + str(self.autor)

    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))


# etiquetas
#etiquetas

class e_g(models.Model):
    Gamer=models.TextField()
    correo=models.EmailField()

class e_l(models.Model):
    LGBTQ=models.TextField()
    correo=models.EmailField()

class e_m(models.Model):
    Música=models.TextField()
    correo=models.EmailField()

class e_a(models.Model):
    Anime=models.TextField()
    correo=models.EmailField()

class e_d(models.Model):
    Deportista=models.TextField()
    correo=models.EmailField()

class e_t(models.Model):
    Tecnología=models.TextField()
    correo=models.EmailField()

class e_jm(models.Model):
    jm=models.TextField()
    correo=models.EmailField()

class e_p(models.Model):
    ep=models.TextField()
    correo=models.EmailField()

class e_s(models.Model):
    Soltero=models.TextField()
    correo=models.EmailField()

class e_c(models.Model):
    Cinéfilo=models.TextField()
    correo=models.EmailField()

class e_k(models.Model):
    Kpop=models.TextField()
    correo=models.EmailField()

class e_pp(models.Model):
    pp=models.TextField()
    correo=models.EmailField()

class e_pg(models.Model):
    pg=models.TextField()
    correo=models.EmailField()

# Amigos

class amigos(models.Model):
    correo = models.EmailField()
    list_amigos=models.TextField()
