from django.shortcuts import render

# Create your views here.

def about(request):
    """ A view that renders the about me page """
    return render(request, 'about/about.html', {'title': 'About'})

def portafolio(request):
    """ A view that renders the portafolio page """
    return render(request, 'about/my_portafolio.html', {'title': 'Portafolio'})

def connect(request):
    """ A view that renders the portafolio page """
    return render(request, 'about/connect.html', {'title': 'Connect'})