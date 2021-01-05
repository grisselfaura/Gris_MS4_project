from django.shortcuts import get_object_or_404
from products.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, select_date, quantity in bag.items():
        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'select_date': select_date,
            'quantity': quantity,
            'service': service,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
