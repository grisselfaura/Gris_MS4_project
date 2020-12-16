from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Service, Category
from .forms import ProductForm

# Create your views here.


def all_services(request):
    """ A view to show all services, including sorting and search queries """

    all_services = Service.objects.all()
    # query and categories will be set to empty when page is first load to avoid errors
    query = None
    categories = None
    sort = None
    direction = None

    # When more services are added by the website owner this functionality will help the end users.
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                all_services = all_services.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            all_services = all_services.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            all_services = all_services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'services': all_services,
        'search_word': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/services.html', context)


def service_detail(request, service_id):
    """ A view to show individual service details """

    service_detail = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service_detail,
    }
    return render(request, 'products/service_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
