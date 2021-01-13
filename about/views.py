from django.shortcuts import render, get_object_or_404

from .models import Portfolio


def about(request):
    """ A view that renders the about me page """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'about/about.html', context)


def portfolio(request):
    """ A view that renders the individual portafolio project details  """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'about/portfolio.html', context)


def connect(request):
    """ A view that renders the portafolio page """
    return render(request, 'about/connect.html', {'title': 'Connect'})


def portfolio_detail(request, portfolio_id):
    """ A view that renders the individual portafolio project details  """

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'about/portfolio_slide_vertical.html', context)


