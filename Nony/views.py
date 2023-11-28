from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
from django.shortcuts import render
from Usuarios.models import persona
from django.contrib import messages


def pag(request):
    return render(request, 'pag.html')

def home(request):
    return render(request, "home.html")

def regis(request):
    if request.method == 'POST':
        nombre=request.POST['nom']
        correo=request.POST['mail']
        contra=request.POST['pass']
        persona(nombre=nombre, mail=correo, pas=contra).save()
        messages.success(request, 'El usuario se creo exitosamente')
        return render(request, 'registro.html')
    else:   
        return render(request, 'registro.html')
    
def login(request):
    if request.method == 'POST':
        try:
            usu_existente= persona.objects.get(mail=request.POST['e_mail'], pas=request.POST['password'])
            request.session['mail']=usu_existente.mail
            return render(request, 'home.html')
        except usu_existente.DoesNotExist as e:
            messages.success(request, 'Alguno de los apartados es incorrecto o no existe')
    return render(request, 'login.html')

def salir(request):
    try:
        del request.session['mail']
    except:
        return render(request, 'pag.html')
    return render(request, 'pag.html')
