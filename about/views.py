from django.shortcuts import render, get_object_or_404

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


def portfolio_detail(request):
    """ A view that renders the indiviadual portafolio project details  """
    return render(request, 'about/my_portafolio_slide_show.html',
                    {'title': 'Portfolio_detail'})

# def portafolio_detail(request, portafolio_id):
#     """ A view that renders the indiviadual portafolio project details """

#     portafolio_detail = get_object_or_404(Portafolio, pk=portafolio_id)

#     context = {
#         'portafolio': portafolio_detail,
#     }
#     return render(request, 'about/my_portafolio_slide_show.html', context)
