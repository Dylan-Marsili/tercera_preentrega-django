from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "AppClinica/index.html")

def empleados(request):
    return render(request, "AppClinica/empleados.html", {'empleados': Empleado.objects.all()})

def citas(request):
    return render(request, "AppClinica/citas.html", {'citas': Cita.objects.all()})

def clientes(request):
    return render(request, "AppClinica/clientes.html", {'clientes': Cliente.objects.all()})

def clientes_habu(request):
    
    if request.method == 'POST':
        
        form = ClienteForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            cliente = Cliente(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            
            cliente.save()
            
            return render(request, "AppClinica/index.html")
    else:
        form = ClienteForm()
    
    return render(request, "AppClinica/clientes_habu.html", {'form': form})

def empleados_habu(request):
    
    if request.method == 'POST':
        
        form = EmpleadoForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            empleado = Empleado(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], cargo=info['cargo'])
            
            empleado.save()
            
            return render(request, "AppClinica/index.html")
    else:
        form = EmpleadoForm()
    
    return render(request, "AppClinica/empleados_habu.html", {'form': form})

def citas_habu(request):
    
    if request.method == 'POST':
        
        form = CitaForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            
            cita = Cita(nombrep=info['nombrep'], fecha=info['fecha'])
            
            cita.save()
            
            return render(request, "AppClinica/index.html")
    else:
        form = CitaForm()
    
    return render(request, "AppClinica/citas_habu.html", {'form': form})

def response(request):
    try:
        if request.GET['email']:
            
            email = request.GET['email']
            clientesf = Cliente.objects.filter(email__icontains=email)
            
            return render(request, 'AppClinica/response.html', {'clientes': clientesf, 'email': email, 'type': 'clientes'})
    except:
        pass
    try:
        if request.GET['cargo']:
            
            cargo = request.GET['cargo']
            empleadof = Empleado.objects.filter(cargo__icontains=cargo)
            
            return render(request, 'AppClinica/response.html', {'empleados': empleadof, 'cargo': cargo, 'type': 'empleados'})
    except:
        pass

    try:
        if request.GET['nombrep']:
            
            nombrep = request.GET['nombrep']
            citaf = Cita.objects.filter(nombrep__icontains=nombrep)
            
            return render(request, 'AppClinica/response.html', {'citas': citaf, 'nombrep': nombrep, 'type': 'citas'})
    except:
        pass
    
    respuesta = 'ERROR, data was not found'
    
    return HttpResponse(respuesta)
