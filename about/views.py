from django.shortcuts import render, get_object_or_404

from .models import Portfolio

# Create your views here.


def about(request):
    """ A view that renders the about me page """
    return render(request, 'about/about.html', {'title': 'About'})


def portfolio(request):
    """ A view that renders the portafolio page """
    return render(request, 'about/my_portafolio.html', {'title': 'Portafolio'})


def connect(request):
    """ A view that renders the portafolio page """
    return render(request, 'about/connect.html', {'title': 'Connect'})


def portfolio_test(request):
    """ A view that renders the individual portafolio project details  """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'about/my_portafolio_copy.html', context)


def portfolio_detail(request):
    """ A view that renders the individual portafolio project details  """
    return render(request, 'about/my_portafolio_slide_show.html',
                    {'title': 'Portfolio_detail'})




# def portfolio_detail(request, portfolio_id):
#     """ A view that renders the indiviadual portafolio project details """

#     portfolio_detail = get_object_or_404(Portafolio, pk=portafolio_id)

#     context = {
#         'portfolio': portfolio_detail,
#     }
#     return render(request, 'about/my_portafolio_slide_show.html', context)
