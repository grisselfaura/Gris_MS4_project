from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Service

# Create your views here.


def all_services(request):
    """ A view to show all services, including sorting and search queries """

    all_services = Service.objects.all()
    # query and categories will be set to empty when page is first load to avoid errors
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            # if the query is blank, the following error message will be displayed
            if not query:
                messages.error(request, "You didn't enter any search words!")
                return redirect(reverse('products'))

            # if query is not blank -> by using q we can search by name OR description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # pass the query to the filter method in order to filter products
            all_services = all_services.filter(queries)

    context = {
        'services': all_services,
        'search_word': query,
    }
    return render(request, 'products/services.html', context)


def service_detail(request, service_id):
    """ A view to show individual service details """

    service_detail = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service_detail,
    }
    return render(request, 'products/service_detail.html', context)
