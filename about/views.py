from django.shortcuts import render

# Create your views here.

def about(request):
    """ A view that renders the about me page """
    return render(request, 'about/about.html', {'title': 'About'})
