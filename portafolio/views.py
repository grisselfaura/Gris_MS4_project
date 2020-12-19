from django.shortcuts import render

# Create your views here.

def portafolio(request):
    """ A view that renders the about me page """
    return render(request, 'portafolio/portafolio.html', {'title': 'Portafolio'})
