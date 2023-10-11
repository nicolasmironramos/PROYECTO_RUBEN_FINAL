from django.shortcuts import render , HttpResponse

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")



#dame una serie de paginas que se llamen index, about, services, store, contact, blog, sample

def home(request):
    return HttpResponse("Inicio")

def about(request):
    return HttpResponse("Historia")

def services(request):
    return HttpResponse("Servicios")

def store(request):
    return HttpResponse("Visítanos")

def contact(request):
    return HttpResponse("Contacto")

def blog(request):
    return HttpResponse("Blog")

def sample(request):
    return HttpResponse("Sample")

def login(request):
    return HttpResponse("Login")

def register(request):
    return HttpResponse("Register")

def logout(request):
    return HttpResponse("Logout")

