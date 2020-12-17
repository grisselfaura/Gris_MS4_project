from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Service added successfully!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, service_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'products/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_product(request, service_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('products'))
