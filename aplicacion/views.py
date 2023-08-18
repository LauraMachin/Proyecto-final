from contextlib import _RedirectStream, redirect_stderr, redirect_stdout
from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView



# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def cliente(request):
    return render(request, "aplicacion/cliente.html")

def top(request):
    return render(request, "aplicacion/top.html")

def camisas(request):
    return render(request, "aplicacion/camisas.html")


def short(request):
    ctx = {"marca": "Zara", "Talle":36}
    return render(request, "aplicacion/short.html", ctx)

def camperas(request):
    return render(request, "aplicacion/camperas.html")

def championes(request):
    return render(request, "aplicacion/championes.html")

def clienteForm(request):
    if request.method == "POST":    
        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], telefono=request.POST['telefono'])
        cliente.save()
        return HttpResponse("Registrado exitosamente")
    
    return render(request, "aplicacion/clienteForm.html")

def clienteForm2(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'])
            cliente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClienteForm()
    return render(request, "aplicacion/clienteForm2.html", {"form":miForm})



def pantalones(request):
    ctx = {'pantalones': Pantalones.objects.all()}
    return render(request, "aplicacion/pantalones.html", ctx)


def updatePantalones(request, id_pantalones):
    pantalones = Pantalones.objects.get(id=id_pantalones)
    if request.methood == 'POST':
        miForm = PantalonesForm(request.POST)
        if miForm.is_valid():
            pantalones.marca = miForm.cleaned_data.get('marca')
            pantalones.talle = miForm.cleaned_data.get('talle')
            pantalones.save()
        return redirect (reverse_lazy({'pantalones'}))
         
    else:
        miForm = PantalonesForm(initial={'marca':pantalones.marca, 'talle':pantalones.talle})  
    return render(request, "aplicacion/pantalonesForm.html", {'form': miForm})

def deletePantalones(request, id_pantalones):
    if request.methood == 'POST':
        miForm = PantalonesForm(request.POST)
        pantalones = Pantalones.objects.get(id=id_pantalones)
        pantalones.delete()
    return redirect (reverse_lazy({'pantalones'}))

def createPantalones(request, id_pantalones):
    if request.methood == 'POST':
        miForm = PantalonesForm(request.POST)
        pantalones = Pantalones.objects.get(id=id_pantalones)
        pantalones.create()
    return redirect (reverse_lazy({'pantalones'}))


class CamperasList(ListView):
      model = Camperas
      template_name = "aplicacion/camperas_list.html"
    




   






