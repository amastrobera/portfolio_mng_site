#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import User, Portfolio, Security

def index(request):    
    #return HttpResponse("Hello, world. You're at the port mng APP index.")
    template = 'portfolio_mng_app/index.html'
    return render(request, template)

def popup_add(request):    
    template = 'portfolio_mng_app/popup_add.html'
    return render(request, template)

def popup_edit(request):    
    template = 'portfolio_mng_app/popup_edit.html'
    return render(request, template)

def popup_delete(request):    
    template = 'portfolio_mng_app/popup_delete.html'
    return render(request, template)

def all_portfolios(request):
    #returns all portfolios in database
    all_port = Portfolio.objects.order_by('-last_update_date')
    context = {'portfolios' : all_port}
    template = 'portfolio_mng_app/portfolios.html'
    return render(request, template, context)

def all_portfolios_per_user(request, ownerId):
    #returns all portfolios owned by a user.id
    #all_port = Portfolio.objects.all().filter(owner__id=pk)
    all_port = get_object_or_404(Portfolio, owner__id=ownerId)
    all_port = all_port.order_by('-last_update_date')
    context = {'portfolios' : all_port}
    template = 'portfolio_mng_app/portfolios.html'
    return render(request, template, context)
    
def all_securities_in_port(request, portfolioId):
    #return all securities in a portfolio, given pk=portfolio.id
    all_secu = get_object_or_404(Security, portfolio__id=portfolioId)
    all_secu = all_secu.order_by('-yid')
    context = {'securities' : all_secu}
    template = 'portfolio_mng_app/securities.html'
    return render(request, template, context)

