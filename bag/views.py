from django.shortcuts import render, redirect, \
 reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Service

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    all_services = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    select_date = None
    if 'select_date' in request.POST:
        select_date = request.POST['select_date']
    # Most clients customers would order one service at the time
    if item_id in list(bag.keys()):
        # If same product and same time selected
        if select_date in bag[item_id]['items_by_date'].keys():
            messages.error(request, f'{all_services.name} scheduled for {select_date} already in your bag! \
                Please book a different timeslot for your next order')
            return redirect(redirect_url)
        # If same product and diferent time selected
        else:
            messages.info(request, f'{all_services.name} already in your bag! \
                Please give me a call to discuss the posibilities')
            return redirect(redirect_url)
    else:
        if bag != {}:
            for item in list(bag):
                # different product same time
                if select_date in bag[item]['items_by_date'].keys():
                    messages.error(request, f' other service scheduled for {select_date} already in your bag! \
                        Please book a different timeslot for your next order')
                    return redirect(redirect_url)
                # different product different time
                else:
                    bag[item_id] = {'items_by_date': {select_date: quantity}}
                    messages.success(request, f'Added {all_services.name} to your bag')
        else:
            bag[item_id] = {'items_by_date': {select_date: quantity}}
            messages.success(request, f'Added {all_services.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    all_services = get_object_or_404(Service, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    select_date = None
    if 'select_date' in request.POST:
        select_date = request.POST['select_date']

    if select_date == select_date in bag[item_id]['items_by_date'].keys():
        if quantity > 0:
            bag[item_id] = {'items_by_date': {select_date: quantity}}
            messages.success(
                request, f'Updated Successfully {all_services.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {all_services.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        all_services = get_object_or_404(Service, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {all_services.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)



# if select_date == select_date:
#     if item_id in list(bag.keys()):
#         # If same product and same time selected
#         messages.error(request, f'{all_services.name} scheduled for {select_date} already in your bag! \
#             Please book a different timeslot for your next order')
#         return redirect(redirect_url)
#         # If same product and diferent time selected
#     else:
#         messages.info(request, f'{all_services.name} already in your bag! \
#             Please give me a call to discuss the posibilities')
#         return redirect(redirect_url)
# else:
#     # if different product same time
#     if item_id not in list(bag.keys()):
#         messages.error(request, f' other service scheduled for {select_date} already in your bag! \
#             Please book a different timeslot for your next order')
#         return redirect(redirect_url)
#     # different product different time
#     else:
#         bag[item_id] = {'items_by_date': {select_date: quantity}}
#         messages.success(request, f'Added {all_services.name} to your bag')
    