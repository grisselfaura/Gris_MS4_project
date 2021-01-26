from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def view_404(request, exception):
    return render(request, 'templates/404.html')


def view_500(request):
    return render(request, 'templates/500.html')
