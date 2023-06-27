from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registrarse.html')

def contacto(request):
    return render(request,'contacto.html')

def nosotros(request):
    return render(request,'sobre_nosotros.html')

def herramientas(request):
    return render(request,'herramientas.html')

def accesorios(request):
    return render(request,'accesorios.html')

def construccion(request):
    return render(request,'productos_construccion.html')