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
    context = {
        "title": "Home",
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "title": "about",
    }
    return render(request, "about.html", context)

def services(request):

    context = {
        "title": "Django example",
    }
    return render(request, "services.html", context)

def store(request):
    
    context = {
        "title": "Django example",
    }
    return render(request, "store.html", context)

def contact(request):
    context = {
        "title": "Contact",
    }
    return render(request, "contact.html", context)

def blog(request):
    context = {
        "title": "Blog",
    }
    return render(request, "blog.html", context)

def sample(request):
    context = {
        "title": "Sample",
    }
    return render(request, "sample.html", context)


