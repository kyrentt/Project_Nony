from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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

    def __str__(self):
        return self.titulo + " | " + str(self.autor)

    def get_absolute_url(self):
        return reverse("article-detail", args=(str(self.id)))


# etiquetas


class e_g(models.Model):
    Gamer = models.TextField()
    correo = models.EmailField()


class e_l(models.Model):
    LQBTQ = models.TextField()
    correo = models.EmailField()


class e_m(models.Model):
    Musica = models.TextField()
    correo = models.EmailField()


class e_o(models.Model):
    Otaku = models.TextField()
    correo = models.EmailField()


class e_d(models.Model):
    Deportista = models.TextField()
    correo = models.EmailField()


# Amigos
