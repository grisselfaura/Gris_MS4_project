from django.shortcuts import render
from .models import Service

# Create your views here.


def all_services(request):
    """ A view to show all products, including sorting and search queries """

    all_services = Service.objects.all()

    context = {
        'services': all_services
    }
    return render(request, 'products/services.html', context)

